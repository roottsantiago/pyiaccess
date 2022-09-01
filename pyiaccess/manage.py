#!/usr/bin/env python
import os
from dotenv import load_dotenv
from pathlib import Path


def set_env(path_env):
    """
    Define the environment variables for the application.
    """
    dotenv_path = Path(path_env)
    load_dotenv(dotenv_path=dotenv_path)
