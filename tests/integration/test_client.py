# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import pytest

if TYPE_CHECKING:
    from re3data import Client


@pytest.mark.default_cassette("repositories.yaml")
@pytest.mark.vcr()
def test_client_list_repositories_default_return_type(client: Client) -> None:
    response = client.repositories.list()
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="UTF-8"?>' in response
    assert "<list>" in response
    assert "<repository>" in response


@pytest.mark.default_cassette("repositories.yaml")
@pytest.mark.vcr()
def test_client_list_repositories_invalid_return_type(client: Client) -> None:
    with pytest.raises(ValueError, match="Invalid `return_type`"):
        client.repositories.list(return_type="json")


@pytest.mark.default_cassette("repositories.yaml")
@pytest.mark.vcr()
def test_client_list_repositories_xml(client: Client) -> None:
    response = client.repositories.list(return_type="xml")
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="UTF-8"?>' in response
    assert "<list>" in response
    assert "<repository>" in response


@pytest.mark.default_cassette("repositories.yaml")
@pytest.mark.vcr()
def test_client_list_repositories_response(client: Client) -> None:
    response = client.repositories.list(return_type="response")
    assert isinstance(response, httpx.Response)
    assert response.status_code == httpx.codes.OK


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_client_get_single_repository_default_return_type(client: Client, zenodo_id: str) -> None:
    response = client.repositories.get(zenodo_id)
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="utf-8"?>' in response
    assert "<r3d:repository>" in response
    assert "<r3d:re3data.orgIdentifier>r3d100010468</r3d:re3data.orgIdentifier>" in response


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_client_get_single_repository_xml(client: Client, zenodo_id: str) -> None:
    response = client.repositories.get(zenodo_id, return_type="xml")
    assert isinstance(response, str)
    assert '<?xml version="1.0" encoding="utf-8"?>' in response
    assert "<r3d:repository>" in response
    assert "<r3d:re3data.orgIdentifier>r3d100010468</r3d:re3data.orgIdentifier>" in response


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_client_get_single_repository_response(client: Client, zenodo_id: str) -> None:
    response = client.repositories.get(zenodo_id, return_type="response")
    assert isinstance(response, httpx.Response)
    assert response.status_code == httpx.codes.OK


@pytest.mark.default_cassette("repository.yaml")
@pytest.mark.vcr()
def test_client_get_invalid_repository_id(client: Client) -> None:
    with pytest.raises(httpx.HTTPStatusError):
        client.repositories.get("XXX")


@pytest.mark.default_cassette("repositories.yaml")
@pytest.mark.vcr()
def test_client_package_import() -> None:
    import re3data

    response = re3data.repositories.list(return_type="response")
    assert isinstance(response, httpx.Response)
    assert response.status_code == httpx.codes.OK
