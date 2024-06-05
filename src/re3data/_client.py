# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _client module provides a client for interacting with the re3data API."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal, overload

import httpx

from re3data import __version__
from re3data._exceptions import RepositoryNotFoundError
from re3data._response import Response, _build_response, _parse_repositories_response, _parse_repository_response

if TYPE_CHECKING:
    from re3data._resources import Repository, RepositorySummary

logger = logging.getLogger(__name__)

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


def log_response(response: httpx.Response) -> None:
    """Log the details of an HTTP response.

    This function logs the HTTP method, URL, and status code of the response for debugging purposes.
    It uses the 'debug' logging level to provide detailed diagnostic information.

    Args:
        response: The response object received from an HTTP request.

    Returns:
        None
    """
    logger.debug(
        "[http] Response: %s %s - Status %s", response.request.method, response.request.url, response.status_code
    )


@overload
def _dispatch_return_type(
    response: Response, resource_type: Literal[ResourceType.REPOSITORY], return_type: ReturnType
) -> Repository | Response | str: ...
@overload
def _dispatch_return_type(
    response: Response, resource_type: Literal[ResourceType.REPOSITORY_LIST], return_type: ReturnType
) -> list[RepositorySummary] | Response | str: ...


def _dispatch_return_type(
    response: Response, resource_type: ResourceType, return_type: ReturnType
) -> Repository | list[RepositorySummary] | Response | str:
    """Dispatch the response to the correct return type based on the provided return type and resource type.

    Args:
        response: The response object.
        resource_type: The type of resource being processed.
        return_type: The desired return type for the API resource.

    Returns:
        Depending on the return_type and resource_type, this can be a Repository object, a list of RepositorySummary
            objects, an HTTP response, or the original XML.
    """
    if return_type == ReturnType.DATACLASS:
        if resource_type == ResourceType.REPOSITORY_LIST:
            return _parse_repositories_response(response)
        if resource_type == ResourceType.REPOSITORY:
            return _parse_repository_response(response)
    if return_type == ReturnType.XML:
        return response.text
    return response


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


class RepositoryManager:
    """A manager for interacting with repositories in the re3data API.

    Attributes:
        _client: The client used to make requests.
    """

    def __init__(self, client: Client) -> None:
        self._client = client

    def list(self, return_type: ReturnType = ReturnType.DATACLASS) -> list[RepositorySummary] | Response | str:
        """List the metadata of all repositories in the re3data API.

        Args:
            return_type: The desired return type for the API resource. Defaults to `ReturnType.DATACLASS`.

        Returns:
            Depending on the `return_type`, this can be a list of RepositorySummary objects, an HTTP response,
                or the original XML.

        Raises:
            ValueError: If an invalid `return_type` is provided.
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
        """
        is_valid_return_type(return_type)
        response = self._client._request(Endpoint.REPOSITORY_LIST.value)
        return _dispatch_return_type(response, ResourceType.REPOSITORY_LIST, return_type)

    def get(self, repository_id: str, return_type: ReturnType = ReturnType.DATACLASS) -> Repository | Response | str:
        """Get the metadata of a specific repository.

        Args:
            repository_id: The identifier of the repository to retrieve.
            return_type: The desired return type for the API resource. Defaults to `ReturnType.DATACLASS`.

        Returns:
            Depending on the `return_type`, this can be a Repository object, an HTTP response, or the original XML.

        Raises:
            ValueError: If an invalid `return_type` is provided.
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
            RepositoryNotFoundError: If no repository with the given ID is found.
        """
        is_valid_return_type(return_type)
        response = self._client._request(Endpoint.REPOSITORY.value.format(repository_id=repository_id))
        if response.status_code == httpx.codes.NOT_FOUND:
            raise RepositoryNotFoundError(f"No repository with id '{repository_id}' available at {response.url}.")
        return _dispatch_return_type(response, ResourceType.REPOSITORY, return_type)


class BaseClient(ABC):
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
            event_hooks={"response": [log_response]},
        )

    @abstractmethod
    def _request(self, path: str) -> Response:
        pass


class Client(BaseClient):
    """A client that interacts with the re3data API.

    Attributes:
        _client: The underlying HTTP client.
        _repository_manager: The repository manager to retrieve metadata from the repositories endpoints.

    Examples:
        >>> client = Client():
        >>> response = re3data.repositories.list()
        >>> response
        [RepositorySummary(id='r3d100010468', doi='https://doi.org/10.17616/R3QP53', name='Zenodo', link=Link(href='https://www.re3data.org/api/beta/repository/r3d100010468', rel='self'))]
        ... (remaining repositories truncated)
    """

    _client: httpx.Client

    def __init__(self) -> None:
        super().__init__(httpx.Client)
        self._repository_manager: RepositoryManager = RepositoryManager(self)

    def _request(self, path: str) -> Response:
        """Send a HTTP GET request to the specified API endpoint.

        Args:
            path: The path to send the request to.

        Returns:
            The response object from the HTTP request.

        Raises:
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
            RepositoryNotFoundError: If the `repository_id` is not found.
        """
        http_response = self._client.get(path)
        if http_response.is_server_error:
            http_response.raise_for_status()
        return _build_response(http_response)

    @property
    def repositories(self) -> RepositoryManager:
        """Get the repository manager for this client.

        Returns:
            The repository manager.
        """
        return self._repository_manager
