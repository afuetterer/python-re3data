# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The base module provides base class for clients to interact with the re3data API."""

from __future__ import annotations

from enum import Enum
from typing import Any

import httpx

from re3data import __version__

BASE_URL: str = "https://www.re3data.org/api/beta/"
DEFAULT_HEADERS: dict[str, str] = {
    "Accept": "text/xml; charset=utf-8",
    "User-Agent": f"python-re3data/{__version__}",
}
DEFAULT_TIMEOUT = httpx.Timeout(timeout=10.0)  # timeout in seconds


class Endpoint(str, Enum):
    REPOSITORY = "repository/{repository_id}"
    REPOSITORY_LIST = "repositories"


class ResourceType(str, Enum):
    REPOSITORY = "repository"
    REPOSITORY_LIST = "repositories"


class ReturnType(str, Enum):
    DATACLASS = "dataclass"
    RESPONSE = "response"
    XML = "xml"


def is_valid_return_type(return_type: Any) -> None:
    """Validate if the given return type is valid.

    Args:
        return_type: The return type to validate.

    Returns:
        None

    Raises:
        ValueError: If the given return type is not one of the allowed types.
    """
    allowed_types = [return_type.value for return_type in ReturnType]
    if not isinstance(return_type, ReturnType):
        raise ValueError(f"Invalid value for `return_type`: {return_type} is not one of {allowed_types}.")


def _build_query_params(query: str | None = None) -> dict[str, str]:
    """Build query parameters based on the input query string.

    Args:
        query: The input query string. Defaults to None.

    Returns:
        A dictionary containing the query parameter(s). If no query is provided,
            the function returns an empty dictionary.
    """
    query_params = {}
    if query:
        query_params["query"] = query
    return query_params


class BaseClient:
    """An abstract base class for clients that interact with the re3data API."""

    def __init__(
        self,
        client: type[httpx.Client] | type[httpx.AsyncClient],
    ) -> None:
        self._client = client(
            base_url=BASE_URL,
            headers=DEFAULT_HEADERS,
            timeout=DEFAULT_TIMEOUT,
            follow_redirects=True,
        )
