#!/usr/bin/env sh

REPO_DIR="$(realpath "$(dirname "${0}")/../../")"

shuf -n "${1:-10}" "${REPO_DIR}/data/03/selected21_shigure.txt"
