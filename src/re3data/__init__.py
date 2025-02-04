# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data."""

from importlib.metadata import version

__version__: str = version("python-re3data")

from re3data._client import AsyncClient, Client, ReturnType
from re3data._exceptions import Re3dataError, RepositoryNotFoundError
from re3data._resources import Re3Data, Repository, RepositoryList, RepositorySummary
from re3data._response import Response

__all__ = (
    "AsyncClient",
    "Client",
    "Re3Data",
    "Re3dataError",
    "Repository",
    "RepositoryList",
    "RepositoryNotFoundError",
    "RepositorySummary",
    "Response",
    "ReturnType",
    "__version__",
)

_client = Client()
repositories = _client.repositories
