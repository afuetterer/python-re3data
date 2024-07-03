# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _serializer module offers functions for converting parsed data into dictionaries.

This module provides functions to serialize various types of data into dictionaries.
The serialized data can be used for further processing or storage.

Functions:
    _to_dict: Serialize parsed data into a dictionary.
"""

from typing import Any

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import DictEncoder
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from re3data._resources import Repository, RepositorySummary

CONFIG = SerializerConfig(indent="  ")
CONTEXT = XmlContext()

DICT_ENCODER = DictEncoder(context=CONTEXT, config=CONFIG)


def _to_dict(parsed: Repository | list[RepositorySummary]) -> dict[str, Any]:
    """Serialize parsed data into a dictionary.

    Args:
        parsed: The input data to be serialized. It can be either a single `Repository` object or a list of
            `RepositorySummary` objects.

    Returns:
        dict[str, Any]: A dictionary representation of the input data.
    """
    return DICT_ENCODER.encode(parsed)  # type: ignore[no-any-return]
