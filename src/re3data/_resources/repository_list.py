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

    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rel: None | str = field(
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

    id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    doi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    link: None | Link = field(
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
