# python-re3data: The Pythonic client for the re3data API.

> ⚠️ Please note that this project is currently under active development. As such, it is considered a work in progress,
> and breaking changes may be introduced at any time. We encourage users to frequently check back for updates and to
> exercise caution when using this project in production environments. Contributions and feedback are welcome to help
> move the project towards a more stable release (v1.0.0).

| __CI__      | [![pre-commit.ci status][pre-commit-ci-badge]][pre-commit-ci-status] [![ci][ci-badge]][ci-workflow] [![coverage][coverage-badge]][ci-workflow] [![codeql][codeql-badge]][codeql-workflow]                                                                                      |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __Docs__    | [![docs][docs-badge]][docs-workflow]                                                                                                                                                                                                                                           |
| __Package__ | [![pypi-status][status-badge]][pypi-url] [![pypi-version][pypi-version-badge]][pypi-url] [![pypi-python-versions][pypi-python-versions-badge]][pypi-url] [![all-downloads][all-downloads-badge]][pepy-tech-url] [![monthly-downloads][monthly-downloads-badge]][pepy-tech-url] |
| __Meta__    | [![doi][doi-badge]][doi-url] [![OpenSSF Scorecard][scorecard-badge]][scorecard-url] [![hatch][hatch-badge]][hatch] [![ruff][ruff-badge]][ruff] [![mypy][mypy-badge]][mypy] [![License][license-badge]][license-url]                                                            |

`python-re3data` is a Python library that simplifies interacting with the [re3data](https://www.re3data.org) (Registry
of Research Data Repositories) [REST API](https://www.re3data.org/api/doc), allowing you to easily retrieve and process
metadata about research data repositories in a convenient and Pythonic way.

```pycon
>>> import re3data
>>> response = re3data.repositories.list()
>>> response
[RepositorySummary(id='r3d100010468', doi='https://doi.org/10.17616/R3QP53', name='Zenodo', link=Link(href='https://www.re3data.org/api/beta/repository/r3d100010468', rel='self'))]
... (remaining repositories truncated)
```

```pycon
>>> response = re3data.repositories.get("r3d100010468")
>>> response
Repository(re3data_org_identifier='r3d100010468', repository_name=RepositoryName(value='Zenodo', language=<Languages.ENG: 'eng'>), additional_name=[], repository_url='https://zenodo.org/', repository_identifier=['FAIRsharing_doi:10.25504/FAIRsharing.wy4egf', 'RRID:SCR_004129', 'RRID:nlx_158614'])
... (remaining fields truncated)
```

## Features

- Pythonic API interactions: Interact with the re3data API in a Pythonic way, without having to worry about low-level
    HTTP requests or XML parsing.
- Repository metadata retrieval: Easily fetch and process metadata about research data repositories using
    `re3data.repositories.list()`.
- Repository details retrieval: Get detailed information about a specific repository using
    `re3data.repositories.get(repository_id)`.
- XML response parsers: API XML responses are parsed into Python dataclasses, providing convenient access to the
    elements of the [re3data.org Schema 2.2 XML Schema](https://www.re3data.org/schema/2-2). This makes it easy to work
    with the rich metadata provided by the API.
- Flexible response options: The response type can be switched between:
    - dataclass (default): Returns a Python dataclass object, allowing convenient access to the element of the re3data
        schema
    - response: Returns a Python object representing the API response
    - original XML: Returns the raw XML response from the API

## Requirements

[Python](https://www.python.org/downloads/) >= 3.10

`python-re3data` is built with:

- **HTTP Requests**: [httpx](https://github.com/encode/httpx), a modern and efficient HTTP client library, handles all
    API interactions.
- **XML Parsing**: [xsdata](https://github.com/tefra/xsdata), a powerful tool for generating Python dataclasses from XML
    schemas, simplifies processing of API responses.
- **Optional CLI**: [typer](https://github.com/tiangolo/typer), a popular library for building command-line interfaces,
    powers the user-friendly interface.

## Installation

You can install `python-re3data` via pip from [PyPI][pypi-url]:

```console
python -m pip install python-re3data
```

or pull the Docker image from [GHCR](https://github.com/afuetterer/python-re3data/pkgs/container/python-re3data):

```console
docker pull ghcr.io/afuetterer/python-re3data:latest
```

For a more detailed guide, see [Installation](https://afuetterer.github.io/python-re3data/latest/install/).

## Documentation

The [documentation][docs-url] is made with [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) and is
hosted by [GitHub Pages](https://docs.github.com/en/pages).

## Similar Projects

There are a couple of similar projects available on GitHub, e.g. via the topic
[re3data](https://github.com/topics/re3data). Among them are these implementations in Python:

| Project                                        | Description                                                                          | Last commit                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| [py3data](https://github.com/J535D165/py3data) | `py3data` is a lightweight and thin Python interface to the beta version of the API. | ![last-commit](https://img.shields.io/github/last-commit/J535D165/py3data) |

## License

`python-re3data` is distributed under the terms of the [MIT License][license-url].

<!-- Refs -->

[all-downloads-badge]: https://static.pepy.tech/badge/python-re3data
[ci-badge]: https://github.com/afuetterer/python-re3data/actions/workflows/main.yml/badge.svg
[ci-workflow]: https://github.com/afuetterer/python-re3data/actions/workflows/main.yml
[codeql-badge]: https://github.com/afuetterer/python-re3data/actions/workflows/codeql.yml/badge.svg
[codeql-workflow]: https://github.com/afuetterer/python-re3data/actions/workflows/codeql.yml
[coverage-badge]: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/afuetterer/adc66df152c473c1aa136557ee8181ca/raw/coverage-badge.json
[docs-badge]: https://github.com/afuetterer/python-re3data/actions/workflows/docs.yml/badge.svg
[docs-url]: https://afuetterer.github.io/python-re3data
[docs-workflow]: https://github.com/afuetterer/python-re3data/actions/workflows/docs.yml
[doi-badge]: https://zenodo.org/badge/DOI/10.5281/zenodo.11264510.svg
[doi-url]: https://doi.org/10.5281/zenodo.11264510
[hatch]: https://github.com/pypa/hatch
[hatch-badge]: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://spdx.org/licenses/MIT.html
[monthly-downloads-badge]: https://static.pepy.tech/badge/python-re3data/month
[mypy]: https://mypy-lang.org
[mypy-badge]: https://img.shields.io/badge/types-mypy-blue.svg
[pepy-tech-url]: https://pepy.tech/project/python-re3data
[pre-commit-ci-badge]: https://results.pre-commit.ci/badge/github/afuetterer/python-re3data/main.svg
[pre-commit-ci-status]: https://results.pre-commit.ci/latest/github/afuetterer/python-re3data/main
[pypi-python-versions-badge]: https://img.shields.io/pypi/pyversions/python-re3data.svg?logo=python&label=Python
[pypi-url]: https://pypi.org/project/python-re3data/
[pypi-version-badge]: https://img.shields.io/pypi/v/python-re3data.svg?logo=pypi&label=PyPI
[ruff]: https://github.com/astral-sh/ruff
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
[scorecard-badge]: https://api.securityscorecards.dev/projects/github.com/afuetterer/python-re3data/badge
[scorecard-url]: https://securityscorecards.dev/viewer/?uri=github.com/afuetterer/python-re3data
[status-badge]: https://img.shields.io/pypi/status/python-re3data?logo=pypi
