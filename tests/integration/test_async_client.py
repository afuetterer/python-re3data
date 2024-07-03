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
    from respx import Route

    from re3data import AsyncClient


async def test_client_list_repositories_default_return_type(
    async_client: AsyncClient, mock_repository_list_route: Route
) -> None:
    response = await async_client.repositories.list()
    assert isinstance(response, list)
    # there are 3 canned repositories in the mocked response
    assert len(response) == 3
    assert isinstance(response[0], RepositorySummary)


async def test_client_list_repositories_dataclass(async_client: AsyncClient, mock_repository_list_route: Route) -> None:
    response = await async_client.repositories.list(return_type=ReturnType.DATACLASS)
    assert isinstance(response, list)
    # there are 3 canned repositories in the mocked response
    assert len(response) == 3
    assert isinstance(response[0], RepositorySummary)


async def test_client_list_repositories_invalid_return_type(async_client: AsyncClient) -> None:
    with pytest.raises(ValueError, match="Invalid value for `return_type`"):
        await async_client.repositories.list(return_type="json")  # type: ignore[arg-type]


async def test_client_list_repositories_xml(async_client: AsyncClient, mock_repository_list_route: Route) -> None:
    response = await async_client.repositories.list(return_type=ReturnType.XML)
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="UTF-8"?>' in response
    assert "<list>" in response
    assert "<repository>" in response


async def test_client_list_repositories_json(async_client: AsyncClient, mock_repository_list_route: Route) -> None:
    response = await async_client.repositories.list(return_type=ReturnType.JSON)
    assert isinstance(response, str)
    assert '"id": "r3d100010371",' in response
    assert '"doi": "https://doi.org/10.17616/R3P594",' in response


async def test_client_list_repositories_dict(async_client: AsyncClient, mock_repository_list_route: Route) -> None:
    response = await async_client.repositories.list(return_type=ReturnType.DICT)
    assert isinstance(response, list)
    repository = response[0]
    assert isinstance(repository, dict)
    assert repository["id"] == "r3d100010371"


async def test_client_list_repositories_response(async_client: AsyncClient, mock_repository_list_route: Route) -> None:
    response = await async_client.repositories.list(return_type=ReturnType.RESPONSE)
    assert isinstance(response, Response)
    assert response.status_code == httpx.codes.OK


async def test_client_list_repositories_query_string(
    async_client: AsyncClient, mock_repository_list_query_route: Route
) -> None:
    response = await async_client.repositories.list(query="biosharing")
    assert isinstance(response, list)
    repository = response[0]
    assert isinstance(repository, RepositorySummary)
    assert repository.id == "r3d100010142"


async def test_client_list_repositories_query_string_returns_empty_list(
    async_client: AsyncClient, mock_repository_list_query_empty_list_route: Route
) -> None:
    response = await async_client.repositories.list(query="XXX")
    assert isinstance(response, list)
    assert response == []


async def test_client_get_single_repository_default_return_type(
    async_client: AsyncClient, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = await async_client.repositories.get(zenodo_id)
    assert isinstance(response, Repository)
    assert response.id == zenodo_id
    assert isinstance(response.repository_name, RepositoryName)
    assert response.repository_name.value == "Zenodo"


async def test_client_get_single_repository_xml(
    async_client: AsyncClient, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = await async_client.repositories.get(zenodo_id, return_type=ReturnType.XML)
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="utf-8"?>' in response
    assert "<r3d:repository>" in response
    assert "<r3d:re3data.orgIdentifier>r3d100010468</r3d:re3data.orgIdentifier>" in response


async def test_client_get_single_repository_json(
    async_client: AsyncClient, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = await async_client.repositories.get(zenodo_id, return_type=ReturnType.JSON)
    assert isinstance(response, str)
    assert "{" in response
    assert '"re3data.orgIdentifier": "r3d100010468",' in response


async def test_client_get_single_repository_dict(
    async_client: AsyncClient, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = await async_client.repositories.get(zenodo_id, return_type=ReturnType.DICT)
    assert isinstance(response, dict)
    assert response["re3data.orgIdentifier"] == zenodo_id


async def test_client_get_single_repository_response(
    async_client: AsyncClient, mock_repository_get_route: Route, zenodo_id: str
) -> None:
    response = await async_client.repositories.get(zenodo_id, return_type=ReturnType.RESPONSE)
    assert isinstance(response, Response)
    assert response.status_code == httpx.codes.OK


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
async def test_client_get_invalid_repository_id(async_client: AsyncClient) -> None:
    with pytest.raises(RepositoryNotFoundError):
        await async_client.repositories.get("XXX")


async def test_client_handles_server_error(async_client: AsyncClient, mock_server_error: Route) -> None:
    with pytest.raises(httpx.HTTPStatusError):
        await async_client.repositories.list()
