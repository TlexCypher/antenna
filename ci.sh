#!/usr/bin/env bash
# CI
uv run --with tox-uv tox -e ruff
uv run --with tox-uv tox -e mypy

# Unit Tests
uv run --with tox-uv tox
