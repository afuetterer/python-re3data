# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

import httpx

from re3data._client.base import (
    BaseClient,
    Endpoint,
    ResourceType,
    ReturnType,
    _build_query_params,
    _dispatch_return_type,
    is_valid_return_type,
)
from re3data._exceptions import RepositoryNotFoundError
from re3data._response import Response, _build_response

if TYPE_CHECKING:
    from re3data._resources import Repository, RepositorySummary

logger = logging.getLogger(__name__)


async def async_log_response(response: httpx.Response) -> None:
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


class AsyncRepositoryManager:
    """A manager for interacting with repositories in the re3data API.

    Attributes:
        _client: The client used to make requests.
    """

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(
        self, query: str | None = None, return_type: ReturnType = ReturnType.DATACLASS
    ) -> list[RepositorySummary] | Response | dict[str, Any] | str:
        """List the metadata of all repositories in the re3data API.

        Args:
            query: A query string to filter the results. If provided, only repositories matching the query
                will be returned.
            return_type: The desired return type for the API resource. Defaults to `ReturnType.DATACLASS`.

        Returns:
            Depending on the `return_type`, this can be a list of RepositorySummary objects, an HTTP response,
                a dictionary representation or the original XML.

        Raises:
            ValueError: If an invalid `return_type` is provided.
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
        """
        is_valid_return_type(return_type)
        query_params = _build_query_params(query)
        response = await self._client._request(Endpoint.REPOSITORY_LIST.value, query_params)
        return _dispatch_return_type(response, ResourceType.REPOSITORY_LIST, return_type)

    async def get(
        self, repository_id: str, return_type: ReturnType = ReturnType.DATACLASS
    ) -> Repository | Response | dict[str, Any] | str:
        """Get the metadata of a specific repository.

        Args:
            repository_id: The identifier of the repository to retrieve.
            return_type: The desired return type for the API resource. Defaults to `ReturnType.DATACLASS`.

        Returns:
            Depending on the `return_type`, this can be a Repository object, an HTTP response,
                a dictionary representation or the original XML.

        Raises:
            ValueError: If an invalid `return_type` is provided.
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
            RepositoryNotFoundError: If no repository with the given ID is found.
        """
        is_valid_return_type(return_type)
        response = await self._client._request(Endpoint.REPOSITORY.value.format(repository_id=repository_id))
        if response.status_code == httpx.codes.NOT_FOUND:
            raise RepositoryNotFoundError(f"No repository with id '{repository_id}' available at {response.url}.")
        return _dispatch_return_type(response, ResourceType.REPOSITORY, return_type)


class AsyncClient(BaseClient):
    """A client that interacts with the re3data API.

    Attributes:
        _client: The underlying HTTP client.
        _repository_manager: The repository manager to retrieve metadata from the repositories endpoints.

    Examples:
        >>> async_client = AsyncClient():
        >>> response = await async_client.repositories.list()
        >>> response
        [RepositorySummary(id='r3d100010468', doi='https://doi.org/10.17616/R3QP53', name='Zenodo', link=Link(href='https://www.re3data.org/api/beta/repository/r3d100010468', rel='self'))]
        ... (remaining repositories truncated)
        >>> response = await async_client.repositories.list(query="biosharing")
        >>> response
        [RepositorySummary(id='r3d100010142', doi='https://doi.org/10.17616/R3WS3X', name='FAIRsharing', link=Link(href='https://www.re3data.org/api/beta/repository/r3d100010142', rel='self'))]
    """

    _client: httpx.AsyncClient

    def __init__(self) -> None:
        super().__init__(httpx.AsyncClient)
        self._client.event_hooks["response"] = [async_log_response]
        self._repository_manager: AsyncRepositoryManager = AsyncRepositoryManager(self)

    async def _request(self, path: str, query_params: dict[str, str] | None = None) -> Response:
        """Send a HTTP GET request to the specified API endpoint.

        Args:
            path: The path to send the request to.
            query_params: Optional URL query parameters to be sent with the HTTP GET request. This dictionary
                contains key-value pairs that will be added as query parameters to the API endpoint specified by path.

        Returns:
            The response object from the HTTP request.

        Raises:
            httpx.HTTPStatusError: If the server returned an error status code >= 500.
            RepositoryNotFoundError: If the `repository_id` is not found.
        """
        http_response = await self._client.get(path, params=query_params)
        if http_response.is_server_error:
            http_response.raise_for_status()
        return _build_response(http_response)

    @property
    def repositories(self) -> AsyncRepositoryManager:
        """Get the repository manager for this client.

        Returns:
            The repository manager.
        """
        return self._repository_manager
