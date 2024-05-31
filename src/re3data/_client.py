# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _client module provides a client for interacting with the re3data API."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from enum import Enum

import httpx

from re3data import __version__

logger = logging.getLogger(__name__)

BASE_URL: str = "https://www.re3data.org/api/beta/"
DEFAULT_HEADERS: dict[str, str] = {
    "Accept": "text/xml; charset=utf-8",
    "User-Agent": f"python-re3data/{__version__}",
}
DEFAULT_TIMEOUT = httpx.Timeout(timeout=10.0)  # timeout in seconds


class ReturnType(str, Enum):
    response = "response"
    xml = "xml"


ALLOWED_RETURN_TYPES = {return_type.value for return_type in ReturnType}


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


class RepositoryManager:
    """A manager for interacting with repositories in the re3data API.

    Attributes:
        _client: The client used to make requests.
    """

    def __init__(self, client: Client) -> None:
        self._client = client

    def list(self, return_type: str = ReturnType.xml.value) -> str | httpx.Response:
        """List the metadata of all repositories in the re3data API.

        Args:
            return_type: The type of response to expect. Defaults to "xml".

        Returns:
            A string representation of the response (if `return_type` is "xml") or the full response object.
        """
        return self._client._request("repositories", return_type)

    def get(self, repository_id: str, return_type: str = ReturnType.xml.value) -> str | httpx.Response:
        """Get the metadata of a specific repository.

        Args:
            repository_id: The identifier of the repository to retrieve.
            return_type: The type of response to expect. Defaults to "xml".

        Returns:
            A string representation of the response (if `return_type` is "xml") or the full response object.
        """
        return self._client._request(f"repository/{repository_id}", return_type)


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
    def _request(self, endpoint: str, return_type: str) -> str | httpx.Response:
        pass


class Client(BaseClient):
    """A client that interacts with the re3data API.

    Attributes:
        _client: The underlying HTTP client.
        _repository_manager: The repository manager to retrieve metadata from the repositories endpoints.

    Examples:
        >>> client = Client():
        >>> response = re3data.repositories.list()
        >>> print(response)
        <?xml version="1.0" encoding="UTF-8"?>
        <list>
        <repository>
            <id>r3d100010468</id>
            <doi>https://doi.org/10.17616/R3QP53</doi>
            <name>Zenodo</name>
            <link href="https://www.re3data.org/api/beta/repository/r3d100010468" rel="self" />
        </repository>
        ... (remaining repositories truncated)
    """

    _client: httpx.Client

    def __init__(self) -> None:
        super().__init__(httpx.Client)
        self._repository_manager: RepositoryManager = RepositoryManager(self)

    def _request(self, endpoint: str, return_type: str) -> str | httpx.Response:
        """Send a HTTP GET request to the specified endpoint.

        Args:
            endpoint: The endpoint to send the request to.
            return_type: The type of response to expect.

        Returns:
            A string representation of the response (if `return_type` is "xml") or the full response object.

        Raises:
            httpx.RequestError: If the request fails or times out.
            ValueError: If an invalid `return_type` is provided.
        """
        if return_type not in ALLOWED_RETURN_TYPES:
            raise ValueError(f"Invalid `return_type`: {return_type}. Expected one of: {ALLOWED_RETURN_TYPES}")
        response = self._client.get(endpoint)
        response.raise_for_status()
        if return_type == "xml":
            return response.text
        return response

    @property
    def repositories(self) -> RepositoryManager:
        """Get the repository manager for this client.

        Returns:
            The repository manager.
        """
        return self._repository_manager
