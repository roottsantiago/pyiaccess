#!/usr/bin/env python
import os
from dotenv import load_dotenv
from pathlib import Path
from pyiaccess.transfer import SFTPClient
from pyiaccess.db import IBMClient


def set_env(path_env):
    """
    Define the environment variables for the application.
    """
    dotenv_path = Path(path_env)
    load_dotenv(dotenv_path=dotenv_path)


def create_sftp(**kwargs):
    sftp = SFTPClient(**kwargs)
    return sftp


def create_db(**kwargs):
    ibm = IBMClient(**kwargs)
    return ibm
