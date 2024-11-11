#!/bin/sh

echo $1

pip install -r dev_requirements.txt
pip install docker
pre-commit install
