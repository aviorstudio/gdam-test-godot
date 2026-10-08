SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.PHONY: help install lint test build check dev stop clean
help:
	@echo 'make check: verified engine import of the empty consumer fixture'
install:
	mise trust .mise.toml
	mise install python actionlint http:cicd-engineering
	mise exec -- python3 scripts/profile.py install
lint:
	mise exec -- actionlint
	mise exec -- python3 scripts/profile.py lint
check: lint
	mise exec -- python3 scripts/profile.py check
test build dev stop:
	@echo '$@: unsupported: empty fixture has no game scene, test suite, export presets or persistent service'
clean:
	mise exec -- python3 -c 'import shutil; shutil.rmtree(".artifacts", ignore_errors=True)'
