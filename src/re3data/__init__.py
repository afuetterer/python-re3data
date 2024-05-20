# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""python-re3data."""

from re3data.__about__ import __version__
from re3data._client import Client

__all__ = [
    "__version__",
    "Client",
]

_client = Client()
repositories = _client.repositories
