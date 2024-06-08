# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

from re3data._resources import RepositorySummary

if TYPE_CHECKING:
    from respx import Route


def test_client_package_import(mock_repository_list_route: Route) -> None:
    import re3data

    response = re3data.repositories.list()
    assert isinstance(response, list)
    assert isinstance(response[0], RepositorySummary)
