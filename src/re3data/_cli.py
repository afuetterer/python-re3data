# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data command line interface."""

import logging
import sys
import typing

from rich import print

import re3data

logger = logging.getLogger(__name__)

try:
    import typer
except ImportError:
    logger.error("`typer` is missing. Please run 'pip install python-re3data[cli]' to use the CLI.")
    sys.exit(1)

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = typer.Typer(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
repositories_app = typer.Typer(no_args_is_help=True)
app.add_typer(repositories_app, name="repository")


def _version_callback(show_version: bool) -> None:
    # Ref: https://typer.tiangolo.com/tutorial/options/version/
    from re3data import __version__

    if show_version:
        typer.echo(f"{__version__}")
        raise typer.Exit


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
def list_repositories() -> None:
    """List the metadata of all repositories in the re3data API."""
    response = re3data.repositories.list()
    print(response)


@repositories_app.command("get")
def get_repository(repository_id: str) -> None:
    """Get the metadata of a specific repository."""
    response = re3data.repositories.get(repository_id)
    print(response)
