#!/usr/bin/env bash

LAMBDA_RUNTIME=3.11
# Depending of your system configuration, just set the lambda path manually this way
# LAMBDA_PATH=$(pwd)
LAMBDA_PATH="//d/dev/repos/git/teams-generator-services/services/add-contestants"

echo "Create package lambda.zip"

docker run --rm -v "${LAMBDA_PATH}":/var/task --entrypoint //bin/bash amazon/aws-lambda-python:${LAMBDA_RUNTIME} -c "set -x && yum install -y zip && pip3.11 install virtualenv && mkdir -p /var/build && zip -R /var/build/lambda.zip '*.py' -x '\.*' 'venv/*' '\*/__pycache__/\*' '\*/.* tests/\*' '\*/tests/\*' 'tmp/\*' && virtualenv /var/lambda && source /var/lambda/bin/activate && pip install -r requirements.txt && cd \`python -c 'import sys; print(sys.path[-1])'\` && zip -q -r /var/build/lambda.zip . -x __pycache__/\* \*/__pycache__/\* && mkdir -p /var/task/build && mv /var/build/lambda.zip /var/task/build"

echo "End create package"