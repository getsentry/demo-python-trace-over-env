#!/usr/bin/env bash

# exit on first error
set -xe

# setting up pytthon. create and activate virtual environment then install requirements
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run Process A (that will start Process B)
python process_a.py
