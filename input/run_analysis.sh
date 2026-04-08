#!/bin/bash

# This script runs the analysis of the bot's performance and generates a report.

# make sure venv is up to date
uv sync

# run analysis using the bot's command line interface
uv run sw-metadata-bot run-analysis --config-file input/config.json