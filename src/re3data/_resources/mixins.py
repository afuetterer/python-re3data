# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The mixins module contains mixin classes for re3data API responses.

These mixins provide common attributes and methods for re3data API response objects.
"""

from typing import Any


class IdMixin:
    re3data_org_identifier: str | None

    @property
    def id(self) -> str | None:
        return self.re3data_org_identifier


class LinkMixin:
    link: Any

    @property
    def href(self) -> str | None:
        if self.link:
            return self.link.href  # type: ignore[no-any-return]
        return None
