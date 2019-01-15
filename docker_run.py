#!/usr/bin/python3 -B
""" This script runs the latest fastai docker container and drops the user into a tmux shell.
"""

import os
import pwd
import re
import subprocess
import sys
import tempfile
import time
import types

DOCKER = "/usr/bin/docker"
DATA_DIR = os.path.expanduser('~/fastai/data')
WORKSPACE_DIR = os.path.expanduser('~/fastai/notebooks/fastai')
PORT = str(8888)
DOCKER_SHELL_COMMAND = "/run.sh"

def main():

    command = [DOCKER,
        "run", "--runtime=nvidia", "--rm", "-it",
        "-v", str(DATA_DIR + ":/data"),
        "-v", str(WORKSPACE_DIR + ":/notebooks/fastai"),
        "-p", str(PORT + ":" + PORT),
        "fastai-docker:latest", DOCKER_SHELL_COMMAND]

    subprocess.call(command)

    sys.stdout.flush()

if __name__ == '__main__':
    sys.exit(main())
