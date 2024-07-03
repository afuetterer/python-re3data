# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _response module offers a structured representation of responses from the re3data API.

Functions:
    _build_response: Build a response object from an HTTP response.
    _parse_repository_response: Parse the response from the re3data API into a Repository object.
    _parse_repositories_response: Parse the response from the re3data API into a list of RepositorySummary objects.

Classes:
    Response: A response received from the re3data API, encapsulating the HTTP response.

Notes:
    The module uses the xsdata library for parsing XML responses.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import httpx
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from re3data._resources import Re3Data, Repository, RepositoryList, RepositorySummary

CONTEXT = XmlContext()
PARSER = XmlParser(context=CONTEXT)


def _build_response(http_response: httpx.Response) -> Response:
    """Build a response object from an HTTP response.

    Args:
        http_response: The HTTP response to build a response from.

    Returns:
        A built response object.
    """
    return Response(
        url=http_response.url,
        status_code=httpx.codes(http_response.status_code),
        text=http_response.text,
        headers=http_response.headers,
    )


def _parse_repository_response(response: Response) -> Repository:
    """Parse the response from the re3data API into a Repository object.

    Args:
        response: The response to parse the repository object from.

    Returns:
        A repository object.
    """
    return PARSER.from_string(response.text, Re3Data).repository[0]


def _parse_repositories_response(response: Response) -> list[RepositorySummary]:
    """Parse the response from the re3data API into a list of RepositorySummary objects.

    Args:
        response: The response to parse the list of repository summary objects from.

    Returns:
        A list of repository summary objects.
    """
    return PARSER.from_string(response.text, RepositoryList).repository


@dataclass(slots=True)
class Response:
    """A response received from the re3data API, encapsulating the HTTP response.

    Attributes:
        url: The URL of the request.
        status_code: The HTTP status code of the response.
        headers: A dictionary-like object containing metadata about the response, such as content type and length.
        text: The text content of the response.
    """

    url: httpx.URL
    status_code: httpx.codes
    headers: httpx.Headers = field(repr=False)
    text: str = field(repr=False)
