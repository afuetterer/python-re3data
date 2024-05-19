# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

import sys
from importlib import reload
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from re3data import __version__
from re3data._cli import app

runner = CliRunner()

HELP_OPTION_NAMES = ("-h", "--help")
VERSION_OPTION_NAMES = ("-V", "--version")


def test_no_args_displays_help() -> None:
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "Options" in result.output
    assert "Show this message and exit" in result.output


@pytest.mark.parametrize("help_option_name", HELP_OPTION_NAMES)
def test_help_option_displays_help(help_option_name: str) -> None:
    result = runner.invoke(app, [help_option_name])
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "Options" in result.output
    assert "Show this message and exit" in result.output


@pytest.mark.parametrize("version_option_name", VERSION_OPTION_NAMES)
def test_version_option_displays_version(version_option_name: str) -> None:
    result = runner.invoke(app, [version_option_name])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_typer_missing_message(caplog: pytest.LogCaptureFixture) -> None:
    # act as if "typer" is not installed
    with patch.dict(sys.modules, {"typer": None}):
        with pytest.raises(SystemExit) as exc_info:
            reload(sys.modules["re3data._cli"])
        assert exc_info.type == SystemExit
        assert exc_info.value.code == 1
        assert "Please run 'pip install python-re3data[cli]'" in caplog.text
