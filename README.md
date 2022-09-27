# Systems i Access client for python
It is a client library for access to IBM System i with ODBC and SSH.

Features
[x] Support for Python 3.

# Installation of dependencies
Before installing pyodbc you must install the packages from Debian/Ubuntu systems.

1.1  INSTALLING ON DEBIAN-BASED LINUX DISTRIBUTIONS.

Install python and odbc modules

```
  sudo apt update
  sudo apt install libpq-dev python-dev python3-dev python3.6-dev
  sudo apt install build-essential
```

Install unixodbc

```
sudo apt install unixodbc-dev unixodbc
```

To connect to IBM iSeries systems we will need to download a .deb file, this library can be downloaded from the IBM page https://www.ibm.com/support/pages/ibm-i-access-client-solutions. So let's create an account, log in, and download the IBM i Access for Linux package.

Copy the downloaded iseries odbc driver to the server and install:
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
IBMI_DSN = YOUR DATABASE
IBMI_HOST = YOUR IP
IBMI_USER = YOUR USER
IBMI_PASSWORD = YOUR PASSWORD
IBMI_PORT = YOUR PORT # Define or not is required

SFTP_HOST = YOUR IP
SFTP_USER = YOUR USER
SFTP_PASSWORD = YOUR PASSWORD
SFTP_PORT = 22 # Default 22 or change port
SFTP_REMOTE_PATH = "/home/"
```

Configuration of environment variables of the project or application

```python
from pyiaccess.manage import set_env

# Define .env file with absolute or complete path.
path_env = '/home/user/proyect/.env'

# Load the environment variables.
set_env(path_env)
```
