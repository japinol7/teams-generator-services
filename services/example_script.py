"""Example script for executing some of the services locally.
The events will be taken from the events folder of each service.
You will need access to the S3 bucket to download and upload the required files.
"""

import os
import subprocess

SERVICE_CLEAR_CONTESTANTS_PATH = os.path.join('.', 'clear-contestants')
SERVICE_CLEAR_TEAMS_PATH = os.path.join('.', 'clear-teams')
SERVICE_ADD_CONTESTANTS_PATH = os.path.join('.', 'add-contestants')
SERVICE_GENERATE_TEAMS_PATH = os.path.join('.', 'generate-teams')

PYTHON_SHELL_NAME = 'python'
LAMBDA_FUNCTION_NAME = 'lambda_function.py'
SERVICE_PREFIX_LOG_MSG = f"\n\n{'-' * 10}\n"

start_dir = os.getcwd()


def run_app(app_path, msg, first=False):
    if not first:
        print(SERVICE_PREFIX_LOG_MSG, end='')

    print(msg)
    os.chdir(app_path)
    res = subprocess.run([PYTHON_SHELL_NAME, LAMBDA_FUNCTION_NAME], check=True)
    print(res)
    os.chdir(start_dir)


def clear_contestants():
    run_app(SERVICE_CLEAR_CONTESTANTS_PATH, "Clear contestants", first=True)


def clear_teams():
    run_app(SERVICE_CLEAR_TEAMS_PATH, "Clear teams")


def add_contestants():
    run_app(SERVICE_ADD_CONTESTANTS_PATH, "Add contestants")


def generate_teams():
    run_app(SERVICE_GENERATE_TEAMS_PATH, "Generate teams")


def main():
    clear_contestants()
    clear_teams()
    add_contestants()
    generate_teams()


if __name__ == "__main__":
    main()
