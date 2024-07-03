# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The base module provides a base class for clients to interact with the re3data API."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any, Literal, overload

import httpx

from re3data import __version__
from re3data._response import Response, _parse_repositories_response, _parse_repository_response
from re3data._serializer import _to_dict, _to_json

if TYPE_CHECKING:
    from re3data._resources import Repository, RepositorySummary

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
    DICT = "dict"
    JSON = "json"
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


@overload
def _dispatch_return_type(
    response: Response, resource_type: Literal[ResourceType.REPOSITORY], return_type: ReturnType
) -> Repository | Response | dict[str, Any] | str: ...
@overload
def _dispatch_return_type(
    response: Response, resource_type: Literal[ResourceType.REPOSITORY_LIST], return_type: ReturnType
) -> list[RepositorySummary] | Response | dict[str, Any] | str: ...


def _dispatch_return_type(
    response: Response, resource_type: ResourceType, return_type: ReturnType
) -> Repository | list[RepositorySummary] | Response | dict[str, Any] | str:
    """Dispatch the response to the correct return type based on the provided return type and resource type.

    Args:
        response: The response object.
        resource_type: The type of resource being processed.
        return_type: The desired return type for the API resource.

    Returns:
        Depending on the return_type and resource_type, this can be a Repository object, a list of RepositorySummary
            objects, an HTTP response, a dictionary representation or the original XML.
    """
    if return_type == ReturnType.RESPONSE:
        return response
    if return_type == ReturnType.XML:
        return response.text

    parsed: Repository | list[RepositorySummary]
    if resource_type == ResourceType.REPOSITORY_LIST:
        parsed = _parse_repositories_response(response)
    if resource_type == ResourceType.REPOSITORY:
        parsed = _parse_repository_response(response)
    if return_type == ReturnType.DATACLASS:
        return parsed

    if return_type == ReturnType.JSON:
        return _to_json(parsed)
    return _to_dict(parsed)


class BaseClient:
    """A base class for clients that interact with the re3data API."""

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
