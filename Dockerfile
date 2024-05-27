# syntax=docker/dockerfile:1

# base
# ----------------------------
FROM python:3.12-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_ROOT_USER_ACTION=ignore

# build stage
# ----------------------------
FROM base as build

WORKDIR /app

RUN python -m pip install build

COPY pyproject.toml .
COPY README.md .
COPY src ./src

RUN python -m build --wheel

# runtime stage
# ----------------------------
FROM base as runtime

ARG VERSION

RUN adduser --group --system --no-create-home re3data

WORKDIR /app

COPY --from=build /app/dist ./dist

RUN python -m pip install "./dist/python_re3data-$VERSION-py3-none-any.whl[cli]"

USER re3data

ENTRYPOINT ["re3data"]
