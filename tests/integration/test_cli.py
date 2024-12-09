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
    from pathlib import Path

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
    assert "RepositorySummary" in result.output
    assert "id='r3d100010371'" in result.output
    assert "doi='https://doi.org/10.17616/R3P594'" in result.output


def test_repository_list_dataclass(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "dataclass"])
    assert result.exit_code == 0
    assert "RepositorySummary" in result.output
    assert "id='r3d100010371'" in result.output
    assert "doi='https://doi.org/10.17616/R3P594'" in result.output


def test_repository_list_xml(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "xml"])
    assert result.exit_code == 0
    assert "<repository>" in result.output
    assert "<id>r3d100010371</id>" in result.output
    assert "<doi>https://doi.org/10.17616/R3P594</doi>" in result.output


def test_repository_list_json(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "json"])
    assert result.exit_code == 0
    assert '"id": "r3d100010371",' in result.output
    assert '"doi": "https://doi.org/10.17616/R3P594",' in result.output


def test_repository_list_dict(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "dict"])
    assert result.exit_code == 0
    assert "'id': 'r3d100010371'," in result.output
    assert "'doi': 'https://doi.org/10.17616/R3P594'," in result.output


def test_repository_list_csv(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "csv"])
    assert result.exit_code == 0
    assert "id,doi,name,link.href," in result.output
    assert "https://doi.org/10.17616/R3P594" in result.output


def test_repository_list_dataframe(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "dataframe"])
    assert result.exit_code == 0
    assert "id" in result.output
    assert "r3d100010371" in result.output
    assert "[3 rows x 5 columns]" in result.output


def test_repository_list_response(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "response"])
    assert result.exit_code == 0
    assert "Response" in result.output
    assert "url=URL('https://www.re3data.org/api/beta/repositories')" in result.output


def test_repository_list_invalid_return_type(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--return-type", "excel"])
    assert result.exit_code == 2
    assert "Error" in result.output
    assert "Invalid value for '--return-type': 'excel'" in result.output


def test_repository_list_query(mock_repository_list_query_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--query", "biosharing"])
    assert result.exit_code == 0
    assert "id='r3d100010142'" in result.output
    assert "doi='https://doi.org/10.17616/R3WS3X'" in result.output


def test_repository_list_query_returns_empty_list(mock_repository_list_query_empty_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "list", "--query", "XXX"])
    assert result.exit_code == 0


def test_repository_list_with_valid_outfile(
    mock_repository_list_route: Route, repository_list_xml: str, tmp_path: Path
) -> None:
    outfile = tmp_path / "list.xml"
    result = runner.invoke(app, ["repository", "list", "--return-type", "xml", "--outfile", str(outfile)])
    assert result.exit_code == 0
    file_content = outfile.read_text()
    assert repository_list_xml in file_content


def test_repository_list_with_dir_as_outfile(mock_repository_list_route: Route, tmp_path: Path) -> None:
    outfile = tmp_path
    result = runner.invoke(app, ["repository", "list", "--outfile", str(outfile)])
    assert result.exit_code == 2
    assert "Error" in result.output
    assert "Invalid value for '--outfile':" in result.output


def test_repository_list_with_existing_outfile_overwrite_yes(
    mock_repository_list_route: Route, repository_list_xml: str, tmp_path: Path
) -> None:
    outfile = tmp_path / "list.xml"
    outfile.write_text("some-content")
    result = runner.invoke(app, ["repository", "list", "--return-type", "xml", "--outfile", str(outfile)], input="y")
    assert result.exit_code == 0
    file_content = outfile.read_text()
    assert repository_list_xml in file_content


def test_repository_list_with_existing_outfile_overwrite_no(
    mock_repository_list_route: Route, repository_list_xml: str, tmp_path: Path
) -> None:
    outfile = tmp_path / "list.xml"
    outfile.write_text("some-content")
    result = runner.invoke(app, ["repository", "list", "--return-type", "xml", "--outfile", str(outfile)], input="N")
    assert result.exit_code == 0
    file_content = outfile.read_text()
    assert "some-content" in file_content
    assert repository_list_xml not in file_content


def test_repository_get_without_repository_id(mock_repository_list_route: Route) -> None:
    result = runner.invoke(app, ["repository", "get"])
    assert result.exit_code == 2
    assert "Missing argument" in result.output


def test_repository_get_with_repository_id_default_return_type(
    mock_repository_get_route: Route, zenodo_id: str
) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id])
    assert result.exit_code == 0
    assert "Repository" in result.output
    assert "re3data_org_identifier='r3d100010468'" in result.output


def test_repository_get_with_repository_id_dataclass(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "dataclass"])
    assert result.exit_code == 0
    assert "Repository" in result.output
    assert "re3data_org_identifier='r3d100010468'" in result.output


def test_repository_get_with_repository_id_xml(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "xml"])
    assert result.exit_code == 0
    assert "<r3d:repository>" in result.output
    assert "<r3d:re3data.orgIdentifier>r3d100010468" in result.output


def test_repository_get_with_repository_id_json(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "json"])
    assert result.exit_code == 0
    assert "{" in result.output
    assert '"re3data.orgIdentifier": "r3d100010468",' in result.output


def test_repository_get_with_repository_id_dict(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "dict"])
    assert result.exit_code == 0
    assert "{" in result.output
    assert "'re3data.orgIdentifier': 'r3d100010468'," in result.output


def test_repository_get_with_repository_id_csv(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "csv"])
    assert result.exit_code == 0
    assert result.exit_code == 0
    assert "re3data.orgIdentifier,additionalName,repositoryURL," in result.output
    assert "r3d100010468" in result.output


def test_repository_get_with_repository_id_dataframe(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "dataframe"])
    assert result.exit_code == 0
    assert "re3data.orgIdentifier" in result.output
    assert "r3d100010468" in result.output
    assert "[1 rows x 43 columns]" in result.output


def test_repository_get_with_repository_id_response(mock_repository_get_route: Route, zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "response"])
    assert result.exit_code == 0
    assert "Response" in result.output
    assert "url=URL('https://www.re3data.org/api/beta/repository/r3d100010468')" in result.output


def test_repository_get_with_repository_id_invalid_return_type(zenodo_id: str) -> None:
    result = runner.invoke(app, ["repository", "get", zenodo_id, "--return-type", "excel"])
    assert result.exit_code == 2
    assert "Error" in result.output
    assert "Invalid value for '--return-type': 'excel'" in result.output


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr
def test_repository_get_with_invalid_repository_id() -> None:
    result = runner.invoke(app, ["repository", "get", "XXX"])
    assert result.exit_code == 1
    assert "No repository with id 'XXX' available" in result.output
