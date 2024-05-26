# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _exceptions module defines exception classes for handling error scenarios encountered when using the re3data API.

Classes:
    Re3dataError: Base exception class for errors related to the re3data API.
    RepositoryNotFoundError: Exception raised when a repository is not found.
"""


class Re3dataError(Exception):
    """Base exception class for errors related to the re3data API."""


class RepositoryNotFoundError(Re3dataError):
    """Exception raised when a repository is not found."""
