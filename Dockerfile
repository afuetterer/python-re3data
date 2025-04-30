# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

# syntax=docker/dockerfile:1.7

# base
# ----------------------------
FROM python:3.13.3-slim@sha256:60248ff36cf701fcb6729c085a879d81e4603f7f507345742dc82d4b38d16784 AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_ONLY_BINARY=:all: \
    PIP_ROOT_USER_ACTION=ignore

# build stage
# ----------------------------
FROM base AS build

ENV BUILD_VERSION=1.2.1

WORKDIR /app

RUN python -m pip install --quiet build[uv]=="$BUILD_VERSION"

COPY pyproject.toml .
COPY README.md .
COPY src ./src

RUN python -m build --installer=uv --wheel

# runtime stage
# ----------------------------
FROM base AS runtime

ARG VERSION

RUN adduser --group --system --no-create-home re3data

COPY --from=build /app/dist ./dist

RUN python -m pip install --quiet "./dist/python_re3data-$VERSION-py3-none-any.whl[cli]" && rm -rf ./dist

USER re3data

ENTRYPOINT ["re3data"]
