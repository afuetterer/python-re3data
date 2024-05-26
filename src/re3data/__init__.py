# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data."""

from re3data.__about__ import __version__
from re3data._client import Client
from re3data._exceptions import Re3dataError, RepositoryNotFoundError

__all__ = [
    "__version__",
    "Client",
    "Re3dataError",
    "RepositoryNotFoundError",
]

_client = Client()
repositories = _client.repositories
