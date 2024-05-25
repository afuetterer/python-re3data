# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

import pytest

from re3data import Client


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
