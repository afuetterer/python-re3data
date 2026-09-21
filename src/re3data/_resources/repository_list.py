# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""API resources for the /repositories endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field

from re3data._resources.mixins import LinkMixin


@dataclass(slots=True)
class Link:
    class Meta:
        name = "link"

    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rel: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class RepositorySummary(LinkMixin):
    class Meta:
        name = "repository"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    doi: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    link: Link | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass(slots=True)
class RepositoryList:
    class Meta:
        name = "list"

    repository: list[RepositorySummary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
