# Installation

## Installing with pip (Recommended)

To install using `pip`, run the following command:

```bash
python -m pip install python-re3data
```

This will automatically install compatible versions of all dependencies, including `httpx` and `xsdata`.

!!! note
    It is highly recommended creating a virtual environment before installing the project. This will help keep your
    dependencies isolated and prevent conflicts with other projects. You can use `venv` to create and manage virtual
    environments.

You can also install optional dependencies, such as the command line interface, by using `pip install python-re3data`
with the `[cli]` flag:

```bash
python -m pip install "python-re3data[cli]"
```

For more details, see [Optional Dependencies](#optional-dependencies).

### Requirements

- Python 3.10 or higher installed on your machine

!!! tip "Alternative: Use uv instead of pip"
    [uv](https://github.com/astral-sh/uv)[^1] is a fast Python package installer and resolver, written in Rust.

    Create a virtual environment in the current directory:

    ```bash
    uv venv
    ```

    Install the project and its dependencies:

    ```bash
    uv pip install python-re3data
    ```

## Pulling the Docker Image

Pull the official image from [GHCR](https://github.com/afuetterer/python-re3data/pkgs/container/python-re3data):

```bash
docker pull ghcr.io/afuetterer/python-re3data:latest
```

!!! note
    The optional `[cli]` dependency group is pre-installed in the Docker image and the `re3data` executable is provided as
    an entry point.

Run the container with:

```bash
$ docker run --rm afuetterer/python-re3data --version
0.5.0
```

!!! tip "Alternative: Use Podman instead of Docker"
    [Podman](https://podman.io/) is an open-source containerization platform that allows you to create, run, and manage
    Linux containers.

    Pull the official image from [GHCR](https://github.com/afuetterer/python-re3data/pkgs/container/python-re3data):

    ```bash
    podman pull ghcr.io/afuetterer/python-re3data:latest
    ```

    Run the container with:

    ```bash
    $ podman run --rm afuetterer/python-re3data --version
    0.5.0
    ```

### Requirements

- Docker[^2] or Podman[^3] installed and running on your machine

## Installing from Source with Git

Clone the repository from GitHub:

```bash
git clone https://github.com/afuetterer/python-re3data.git
```

Change into the directory:

```bash
cd python-re3data
```

Finally, install the project and its dependencies:

```bash
python -m pip install .
```

### Requirements

- Git installed on your machine
- Python 3.10 or higher installed on your machine

## Dependencies

### Required Dependencies

`python-re3data` requires the following dependencies:

| Package                                   | Version | Description                                                                                                    |
| ----------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| [httpx](https://github.com/encode/httpx)  | >= 0.27 | A modern and efficient HTTP client library, handles all API interactions.                                      |
| [xsdata](https://github.com/tefra/xsdata) | >= 24.5 | A powerful tool for generating Python dataclasses from XML    schemas, simplifies processing of API responses. |

### Optional dependencies

#### Command Line Interface

Install with `python -m pip install "python-re3data[cli]"`.

| Package                                    | Version | Description                                                                                 |
| ------------------------------------------ | ------- | ------------------------------------------------------------------------------------------- |
| [typer](https://github.com/tiangolo/typer) | >= 0.12 | A popular library for building command-line interfaces, powers the user-friendly interface. |

<!---
This installation guide is adapted from these sources:
- "pandas" Installation, https://pandas.pydata.org/docs/getting_started/install.html (BSD-3-Clause license)
- "Dask" Installation, https://docs.dask.org/en/stable/install.html (BSD-3-Clause license)
- "Material for MkDocs" Installation, https://squidfunk.github.io/mkdocs-material/getting-started/ (MIT License)
--->

[^1]: For installation instructions, see
    [Getting Started](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started).

[^2]: For installation instructions, see [Install Docker Engine](https://docs.docker.com/engine/install/).

[^3]: For installation instructions, see [Podman Installation Instructions](https://podman.io/docs/installation).
