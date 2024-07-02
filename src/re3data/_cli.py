# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data command line interface."""

import logging
import sys
import typing
from typing import Annotated, Optional

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


@app.callback(context_settings=CONTEXT_SETTINGS)
def callback(
    version: typing.Annotated[
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
        Optional[str],  # noqa: UP007
        typer.Option(
            help="A query to filter the results. If provided, only repositories matching the query will be returned."
        ),
    ] = None,
    return_type: ReturnType = ReturnType.DATACLASS,
) -> None:
    """List the metadata of all repositories in the re3data API."""
    response = re3data.repositories.list(query, return_type)
    console.print(response)


@repositories_app.command("get")
def get_repository(repository_id: str, return_type: ReturnType = ReturnType.DATACLASS) -> None:
    """Get the metadata of a specific repository."""
    try:
        response = re3data.repositories.get(repository_id, return_type)
        console.print(response)
    except RepositoryNotFoundError as error:
        print_error(str(error))
        raise typer.Exit(code=1) from error
