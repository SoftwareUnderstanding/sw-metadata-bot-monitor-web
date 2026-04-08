#!/bin/bash

# This script runs the analysis of the bot's performance and generates a report.

CONFIG_FILE="input/config.json"
# make sure venv is up to date
uv sync

# run analysis using the bot's command line interface
uv run sw-metadata-bot run-analysis --config-file $CONFIG_FILE

OUTPUT_DIR=$(uv run python -c "import read_config; config = read_config.read_config('$CONFIG_FILE'); print(read_config.get_output_folder(config))")
# get latest subfolder created from config file
LATEST_SUBFOLDER=$(ls -td $OUTPUT_DIR/*/ | head -1)

uv run sw-metadata-bot publish --analysis-root $LATEST_SUBFOLDER/