# Systems i Access client for python
It is a client library for access to IBM System i with ODBC and SSH.

Features
[x] Support for Python 3.

# Installation of dependencies
Before installing pyodbc you must install the packages from Debian/Ubuntu systems.

1.1  INSTALLING ON DEBIAN-BASED LINUX DISTRIBUTIONS.

```
  sudo apt update
  sudo apt install libpq-dev python-dev python3-dev
  sudo apt install python3.5-dev python3.6-dev
  sudo apt install unixodbc-dev
  sudo apt install build-essential
```
To connect to IBM iSeries systems we will need to download a .deb file, this library can be downloaded from the IBM page https://www.ibm.com/support/pages/ibm-i-access-client-solutions. So let's create an account, log in, and download the IBM i Access for Linux package.

Example installation instructions:
```
  sudo apt install ./ibm-iaccess-1.1.0.15-1.0.ppc64el.deb
```

Installation
------------

Install pyiaccess.
```python
pip install pyiaccess
```

# Usage
Create a .env file in the root of your project

```
ISERIE_DSN = LIBRARY
ISERIE_HOST = HOST
ISERIE_USER = USER
ISERIE_PASSWORD = PASSWORD

SFTP_PORT = 22
SFTP_REMOTE_PATH = "/home/repo/"
```

Configuration of environment variables of the project or application

```python
import os
from pyiaccess.manage import set_env

# Define .env file with absolute or complete path.
path_env = '/home/user/proyect/.env'

# Define .env file with relative path of the project or application.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_env = os.path.join(BASE_DIR, ".env")

# Load the environment variables.
set_env(path_env)
```
