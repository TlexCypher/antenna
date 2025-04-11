#!/usr/bin/env bash
# CI
tox -e ruff
tox -e mypy

# Unit Tests
tox
