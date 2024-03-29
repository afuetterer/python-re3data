# python-re3data: The pythonic client for the re3data API.

| __CI__ | [![pre-commit.ci status][pre-commit-ci-badge]][pre-commit-ci-status] [![ci][ci-badge]][ci-workflow] [![coverage][coverage-badge]][ci-workflow] |
| :--- | :--- |
| __Docs__ | [![docs][docs-badge]][docs-workflow] |
| __Meta__ | [![OpenSSF Scorecard][scorecard-badge]][scorecard-url] [![hatch][hatch-badge]][hatch] [![ruff][ruff-badge]][ruff] [![mypy][mypy-badge]][mypy] [![License][license-badge]][license-url] |

## Requirements

[Python](https://www.python.org/downloads/) >= 3.10

python-re3data is built with:

- [httpx](https://github.com/encode/httpx) for issuing HTTP requests

## Installation

You can install python-re3data via pip from [PyPI][pypi-url]:

```console
python -m pip install python-re3data
```

## Documentation

The [documentation][docs-url] is made with [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) and is hosted by [GitHub Pages](https://docs.github.com/en/pages).

## License

python-re3data is distributed under the terms of the [MIT License][license-url].

<!-- Markdown links -->
[ci-workflow]: https://github.com/afuetterer/python-re3data/actions/workflows/main.yml
[ci-badge]: https://github.com/afuetterer/python-re3data/actions/workflows/main.yml/badge.svg
[coverage-badge]: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/afuetterer/adc66df152c473c1aa136557ee8181ca/raw/coverage-badge.json
[pre-commit-ci-status]: https://results.pre-commit.ci/latest/github/afuetterer/python-re3data/main
[pre-commit-ci-badge]: https://results.pre-commit.ci/badge/github/afuetterer/python-re3data/main.svg
[docs-url]: https://afuetterer.github.io/python-re3data
[docs-workflow]: https://github.com/afuetterer/python-re3data/actions/workflows/docs.yml
[docs-badge]: https://github.com/afuetterer/python-re3data/actions/workflows/docs.yml/badge.svg
[scorecard-url]: https://securityscorecards.dev/viewer/?uri=github.com/afuetterer/python-re3data
[scorecard-badge]: https://api.securityscorecards.dev/projects/github.com/afuetterer/python-re3data/badge
[pypi-url]: https://pypi.org/project/python-re3data/
[pypi-version-badge]: https://img.shields.io/pypi/v/python-re3data.svg?logo=pypi&label=PyPI
[pypi-downloads-badge]: https://img.shields.io/pypi/dm/python-re3data.svg?color=blue&label=Downloads&logo=pypi
[pypi-python-versions-badge]: https://img.shields.io/pypi/pyversions/python-re3data.svg?logo=python&label=Python
[license-url]: https://spdx.org/licenses/MIT.html
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[hatch]: https://github.com/pypa/hatch
[hatch-badge]: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
[ruff]: https://github.com/astral-sh/ruff
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
[mypy]: https://mypy-lang.org
[mypy-badge]: https://img.shields.io/badge/types-mypy-blue.svg
