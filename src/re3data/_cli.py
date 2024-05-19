"""re3data command line interface."""

import logging
import sys
import typing

logger = logging.getLogger(__name__)

try:
    import typer
except ImportError:
    logger.error("`typer` is missing. Please run 'pip install python-re3data[cli]' to use the CLI.")
    sys.exit(1)

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = typer.Typer(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)


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
        ),
    ] = False,
) -> None:
    """python-re3data."""
