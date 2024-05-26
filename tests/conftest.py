# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT
from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import pytest

from re3data import Client

if TYPE_CHECKING:
    from respx import MockRouter, Route


@pytest.fixture(scope="session")
def vcr_config() -> dict[str, str]:
    return {"cassette_library_dir": "tests/cassettes"}


@pytest.fixture(scope="session")
def client() -> Client:
    return Client()


@pytest.fixture(scope="session")
def zenodo_id() -> str:
    # Ref: https://www.re3data.org/repository/r3d100010468
    return "r3d100010468"


REPOSITORY_LIST_XML: str = """
<?xml version="1.0" encoding="UTF-8"?>
<list>
    <repository>
        <id>r3d100010371</id>
        <doi>https://doi.org/10.17616/R3P594</doi>
        <name>ZACAT</name>
        <link href="https://www.re3data.org/api/beta/repository/r3d100010371" rel="self"/>
    </repository>
    <repository>
        <id>r3d100010376</id>
        <doi>https://doi.org/10.17616/R31G7K</doi>
        <name>Land Processes Distributed Active Archive Center</name>
        <link href="https://www.re3data.org/api/beta/repository/r3d100010376" rel="self"/>
    </repository>
    <repository>
        <id>r3d100010829</id>
        <doi>https://doi.org/10.17616/R3TW4Q</doi>
        <name>India Water Portal</name>
        <link href="https://www.re3data.org/api/beta/repository/r3d100010829" rel="self"/>
    </repository>
</list>
"""


@pytest.fixture()
def mock_repository_list_route(respx_mock: MockRouter) -> Route:
    return respx_mock.get("https://www.re3data.org/api/beta/repositories").mock(
        return_value=httpx.Response(httpx.codes.OK, text=REPOSITORY_LIST_XML)
    )
