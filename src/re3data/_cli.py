# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data command line interface."""

import logging
import sys
from pathlib import Path
from typing import Annotated, Any, Optional

from rich.console import Console

import re3data
from re3data._client import ReturnType
from re3data._exceptions import RepositoryNotFoundError

logger = logging.getLogger(__name__)

try:
    import typer
except ImportError:
    logger.error("`typer` is missing. Please run 'pip install python-re3data[cli]' to use the CLI.")
    sys.exit(1)

console = Console()


def print_error(message: str) -> None:
    """Print an error message to the console in bold red.

    Args:
        message: The error message to be printed.

    Returns:
        None
    """
    console.print(message, style="bold red")


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = typer.Typer(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
repositories_app = typer.Typer(no_args_is_help=True)
app.add_typer(repositories_app, name="repository")


def _version_callback(show_version: bool) -> None:
    # Ref: https://typer.tiangolo.com/tutorial/options/version/
    from re3data import __version__

    if show_version:
        console.print(__version__)
        raise typer.Exit(code=0)


def _write_to_file(response: Any, outfile: Path | None) -> None:
    """Write the given response to the specified file.

    Args:
        response: The response to be written.
        outfile: The path to the output file. If None, no file will be written.

    Returns:
        None
    """
    if outfile and outfile.exists():
        overwrite = typer.confirm(f"{outfile} already exists. Do you want to overwrite it?")
        if not overwrite:
            return
    if outfile:
        outfile.write_text(str(response))


@app.callback(context_settings=CONTEXT_SETTINGS)
def callback(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Show python-re3data version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """python-re3data."""


@repositories_app.command("list")
def list_repositories(
    query: Annotated[
        Optional[str],  # noqa: UP007 - typer does not support "str | None"
        typer.Option(
            help="A query to filter the results. If provided, only repositories matching the query will be returned."
        ),
    ] = None,
    return_type: ReturnType = ReturnType.DATACLASS,
    count: bool = False,
    outfile: Annotated[
        Optional[Path],  # noqa: UP007 - typer does not support "Path | None"
        typer.Option(
            file_okay=True,
            dir_okay=False,
            writable=True,
        ),
    ] = None,
) -> None:
    """List the metadata of all repositories in the re3data API."""
    response = re3data.repositories.list(query, return_type, count)
    _write_to_file(response, outfile)
    console.print(response)


@repositories_app.command("get")
def get_repository(
    repository_id: str,
    return_type: ReturnType = ReturnType.DATACLASS,
    outfile: Annotated[
        Optional[Path],  # noqa: UP007 - typer does not support "Path | None"
        typer.Option(
            file_okay=True,
            dir_okay=False,
            writable=True,
        ),
    ] = None,
) -> None:
    """Get the metadata of a specific repository."""
    try:
        response = re3data.repositories.get(repository_id, return_type)
        console.print(response)
        _write_to_file(response, outfile)
    except RepositoryNotFoundError as error:
        print_error(str(error))
        raise typer.Exit(code=1) from error
