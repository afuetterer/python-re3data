# SPDX-FileCopyrightText: 2025 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import pytest

import re3data
from re3data._resources import Repository, RepositoryName, RepositorySummary

pytestmark = pytest.mark.e2e


def test_get_single_repository(zenodo_id: str) -> None:
    response = re3data.repositories.get(zenodo_id)
    assert isinstance(response, Repository)
    assert response.id == zenodo_id
    assert isinstance(response.repository_name, RepositoryName)
    assert response.repository_name.value == "Zenodo"


def test_list_repositories_query_string() -> None:
    response = re3data.repositories.list(query="biosharing")
    assert isinstance(response, list)
    assert isinstance(response[0], RepositorySummary)
