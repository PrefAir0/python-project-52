#!/usr/bin/env bash
set -o erxit

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

make install && make migrate && make collectstatic