#!/bin/sh

echo $1

pip install -r $1/dev_requirements.txt
pip install docker
pre-commit install