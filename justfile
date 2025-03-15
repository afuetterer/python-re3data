# justfile
# Ref: https://just.systems/man/en/
# ------------------------------------------------------------------------------

_default:
    @just --list --unsorted

sync:
    uv sync --locked

sync-docs:
    uv sync --locked --group=docs

@project-version:
    uv run toml get --toml-path pyproject.toml project.version

pre-commit := "pre-commit run --all-files --color=always --show-diff-on-failure"

[group('lint')]
lint:
    SKIP=mypy uv run {{ pre-commit }}

[group('lint')]
typecheck:
    uv run {{ pre-commit }} mypy

[group('lint')]
check: lint typecheck

[group('test')]
test:
    uv run pytest tests

[group('test')]
cov:
    uv run pytest --cov=src

[group('test')]
cov-report-markdown:
    uv run python -m coverage report --format=markdown > coverage.md

[group('test')]
cov-total:
    uv run python -m coverage json --quiet
    uv run python -c "import json;print(json.load(open('coverage.json'))['totals']['percent_covered_display'])"

config := "--config-file=docs/mkdocs.yml"

[group('docs')]
docs-cli:
    uv run typer src/re3data/_cli.py utils docs --name=re3data --title='Command Line Interface' --output docs/src/cli.md

[group('docs')]
docs-build: docs-cli
    uv run mkdocs build {{ config }}

[group('docs')]
docs-serve: docs-cli
    uv run mkdocs serve {{ config }} --verbose

[group('docs')]
docs-deploy: docs-cli
    uv run mike deploy {{ config }} --push --update-aliases $(just project-version) latest
