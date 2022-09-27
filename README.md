# Systems i Access Client for python
It is a library for access ODBC and SSH from Linux to IBM i (AS400) for python.
To connect to IBM i we will need to download a ".deb" file, this library can be downloaded from the IBM page oficial. 

IBM ODBC driver (login required) https://www.ibm.com/support/pages/ibm-i-access-client-solutions.

Features
[x] Support for Python 3.6

Installation of dependencies
----------------------------
Before installing pyodbc you must install the packages from Debian/Ubuntu systems.

Install python and odbc modules:

```
  sudo apt update
  sudo apt install libpq-dev python-dev python3-dev python3.6-dev
  sudo apt install build-essential
```

Install unixodbc:
```
sudo apt install unixodbc-dev unixodbc
```

Copy the downloaded iseries odbc driver to the server and install:
```
  sudo apt install ./ibm-iaccess-1.1.0.14-1.0.amd64.deb
```

Installation
------------

Install pyiaccess:
```python
pip install PyiAccess
```

Environment Variables
-------
Create a ".env" file at the root of your project to define the environment variables.

```
IBMI_DSN = YOUR DATABASE
IBMI_HOST = YOUR IP
IBMI_USER = YOUR USER
IBMI_PASSWORD = YOUR PASSWORD
IBMI_PORT = YOUR PORT # It is not required

SFTP_HOST = YOUR IP
SFTP_USER = YOUR USER
SFTP_PASSWORD = YOUR PASSWORD
SFTP_PORT = 22 # Default 22 or change port
SFTP_REMOTE_PATH = "/home/" # Define server path to upload files
```

Configuration of environment variables of the project or application.

```python
from pyiaccess.engine import set_env
# Define .env file with absolute or complete path.
path_env = '/home/user/proyect/.env'
# Load the environment variables.
set_env(path_env)
```

Engine Configuration
--------------------
Creating an engine for data base.

```python
from pyiaccess.engine import create_db
engine = create_db(
    hostname=hostname, dsn=dsn, username=username, password=password, port=port
)
engine.connect()
```

Creating an engine for sftp.
```python
from pyiaccess.engine import create_sftp
engine = create_sftp(
    hostname=hostname,
    username=username,
    password=password,
    port=port,
    remote_path=remote_path,
)
engine.connect()
```
