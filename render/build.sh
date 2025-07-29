#!/usr/bin/env bash
echo "Setting Python version to 3.10.12 manually..."
pyenv install -s 3.10.12
pyenv global 3.10.12
pip install -r requirements.txt