# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

"""The _serializer module offers functions for converting parsed data into various return types.

This module provides functions to serialize various types of data, e.g. into dictionaries or JSON strings.
The serialized data can be used for further processing or storage.

Functions:
    _to_dict: Serialize parsed data into a dictionary.
    _to_json: Serialize parsed data into a JSON string.
    _to_dataframe: Serialize parsed data into a DataFrame.
    _to_csv: Serialize parsed data into a CSV string.
"""

from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING, Any

try:
    from pandas import json_normalize

    PANDAS_INSTALLED = True
except ImportError:
    PANDAS_INSTALLED = False

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import DictEncoder, JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

if TYPE_CHECKING:
    from pandas import DataFrame

    from re3data._resources import Repository, RepositorySummary

logger = logging.getLogger(__name__)
CONFIG = SerializerConfig(indent="  ")
CONTEXT = XmlContext()

DICT_ENCODER = DictEncoder(context=CONTEXT, config=CONFIG)
JSON_SERIALIZER = JsonSerializer(context=CONTEXT, config=CONFIG)


def _to_dict(parsed: Repository | list[RepositorySummary]) -> dict[str, Any]:
    """Serialize parsed data into a dictionary.

    Args:
        parsed: The input data to be serialized. It can be either a single `Repository` object or a list of
            `RepositorySummary` objects.

    Returns:
        A dictionary representation of the input data.
    """
    return DICT_ENCODER.encode(parsed)  # type: ignore[no-any-return]


def _to_json(parsed: Repository | list[RepositorySummary]) -> str:
    """Serialize parsed data into a JSON string.

    Args:
        parsed: The input data to be serialized. It can be either a single `Repository` object or a list of
            `RepositorySummary` objects.

    Returns:
        A JSON representation of the input data.
    """
    return JSON_SERIALIZER.render(parsed)


def _to_dataframe(parsed: Repository | list[RepositorySummary]) -> DataFrame:
    """Serialize parsed data into a DataFrame.

    Args:
        parsed: The input data to be serialized. It can be either a single `Repository` object or a list of
            `RepositorySummary` objects.

    Returns:
        A DataFrame representation of the input data.
    """
    if PANDAS_INSTALLED:
        return json_normalize(_to_dict(parsed))
    logger.error("`pandas` is missing. Please run 'pip install python-re3data[csv]'.")
    sys.exit(1)


def _to_csv(parsed: Repository | list[RepositorySummary]) -> str:
    """Serialize parsed data into a CSV string.

    Args:
        parsed: The input data to be serialized. It can be either a single `Repository` object or a list of
            `RepositorySummary` objects.

    Returns:
        A CSV string representation of the input data.
    """
    if PANDAS_INSTALLED:
        return _to_dataframe(parsed).to_csv(index=False)
    logger.error("`pandas` is missing. Please run 'pip install python-re3data[csv]'.")
    sys.exit(1)
