# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import pytest

from re3data import RepositoryNotFoundError, Response, ReturnType
from re3data._resources import Repository, RepositoryName, RepositorySummary

if TYPE_CHECKING:
    from respx import MockRouter, Route

    from re3data import Client


def test_client_list_repositories_default_return_type(client: Client, mock_repository_list_route: Route) -> None:
    response = client.repositories.list()
    assert isinstance(response, list)
    # there are 3 canned repositories in the mocked response
    assert len(response) == 3
    assert isinstance(response[0], RepositorySummary)


def test_client_list_repositories_dataclass(client: Client, mock_repository_list_route: Route) -> None:
    response = client.repositories.list(return_type=ReturnType.DATACLASS)
    assert isinstance(response, list)
    # there are 3 canned repositories in the mocked response
    assert len(response) == 3
    assert isinstance(response[0], RepositorySummary)


def test_client_list_repositories_invalid_return_type(client: Client) -> None:
    with pytest.raises(ValueError, match="Invalid value for `return_type`"):
        client.repositories.list(return_type="json")  # type: ignore[arg-type]


def test_client_list_repositories_xml(client: Client, mock_repository_list_route: Route) -> None:
    response = client.repositories.list(return_type=ReturnType.XML)
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="UTF-8"?>' in response
    assert "<list>" in response
    assert "<repository>" in response


def test_client_list_repositories_response(client: Client, mock_repository_list_route: Route) -> None:
    response = client.repositories.list(return_type=ReturnType.RESPONSE)
    assert isinstance(response, Response)
    assert response.status_code == httpx.codes.OK


def test_client_get_single_repository_default_return_type(
    client: Client, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = client.repositories.get(zenodo_id)
    assert isinstance(response, Repository)
    assert response.id == zenodo_id
    assert isinstance(response.repository_name, RepositoryName)
    assert response.repository_name.value == "Zenodo"


def test_client_get_single_repository_xml(client: Client, mock_repository_get_route: Route, zenodo_id: str) -> None:
    response = client.repositories.get(zenodo_id, return_type=ReturnType.XML)
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="utf-8"?>' in response
    assert "<r3d:repository>" in response
    assert "<r3d:re3data.orgIdentifier>r3d100010468</r3d:re3data.orgIdentifier>" in response


def test_client_get_single_repository_response(
    client: Client, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = client.repositories.get(zenodo_id, return_type=ReturnType.RESPONSE)
    assert isinstance(response, Response)
    assert response.status_code == httpx.codes.OK


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_client_get_invalid_repository_id(client: Client) -> None:
    with pytest.raises(RepositoryNotFoundError):
        client.repositories.get("XXX")


def test_client_package_import(mock_repository_list_route: Route) -> None:
    import re3data

    response = re3data.repositories.list()
    assert isinstance(response, list)
    assert isinstance(response[0], RepositorySummary)


@pytest.fixture()
def mock_server_error(respx_mock: MockRouter) -> Route:
    return respx_mock.get("https://www.re3data.org/api/beta/repositories").mock(
        return_value=httpx.Response(httpx.codes.INTERNAL_SERVER_ERROR)
    )


def test_client_handles_server_error(client: Client, mock_server_error: Route) -> None:
    with pytest.raises(httpx.HTTPStatusError):
        client.repositories.list()
