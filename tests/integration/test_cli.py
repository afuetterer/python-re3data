# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT
from __future__ import annotations

import sys
from importlib import reload
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from re3data import __version__
from re3data._cli import app

if TYPE_CHECKING:
    from respx import Route

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


def test_repository_no_args_displays_help() -> None:
    result = runner.invoke(app, ["repository"])
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "Options" in result.output


def test_repository_list_default_return_type(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list"])
    assert result.exit_code == 0
    assert "<list>" in result.output
    assert "<repository>" in result.output
    assert "<id>" in result.output


def test_repository_list_xml(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "xml"])
    assert result.exit_code == 0
    assert "<list>" in result.output
    assert "<repository>" in result.output
    assert "<id>" in result.output


def test_repository_list_response(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "response"])
    assert result.exit_code == 0
    assert "<Response [200 OK]>" in result.output


def test_repository_list_invalid_return_type(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "json"])
    assert result.exit_code == 2
    assert "Error" in result.output
    assert "Invalid value for '--return-type': 'json'" in result.output


def test_repository_get_without_repository_id(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "get"])
    assert result.exit_code == 2
    assert "Missing argument" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_repository_get_with_repository_id_default_return_type(zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id])
    assert result.exit_code == 0
    assert "<r3d:repository>" in result.output
    assert "<r3d:re3data.orgIdentifier>r3d100010468" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_repository_get_with_repository_id_xml(zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "xml"])
    assert result.exit_code == 0
    assert "<r3d:repository>" in result.output
    assert "<r3d:re3data.orgIdentifier>r3d100010468" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_repository_get_with_repository_id_response(zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "response"])
    assert result.exit_code == 0
    assert "<Response [200 OK]>" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_repository_get_with_repository_id_invalid_return_type(zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "json"])
    assert result.exit_code == 2
    assert "Error" in result.output
    assert "Invalid value for '--return-type': 'json'" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_repository_get_with_invalid_repository_id() -> None:
    result = runner.invoke(app, ["repository", "get", "XXX"])
    assert result.exit_code == 1
