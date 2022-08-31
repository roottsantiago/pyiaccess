# Systems i Access (Sysi)
It is a client library for access to IBM System i systems with ODBC and SSH.

Features
[x] Support for Python 3.

# Installation of dependencies
Before installing pyodbc you must install the packages from Debian/Ubuntu systems.

1.1  INSTALLING ON DEBIAN-BASED LINUX DISTRIBUTIONS.

```
  sudo apt update
  sudo apt install libpq-dev python3-dev
  sudo apt install python3.5-dev python3.6-dev
  sudo apt install unixodbc-dev
  sudo apt install build-essential python-dev
```
To connect to IBM iSeries systems we will need to download a .deb file, this library can be downloaded from the IBM page https://www.ibm.com/support/pages/ibm-i-access-client-solutions. So let's create an account, log in, and download the IBM i Access for Linux package.

Example installation instructions:
```
  sudo apt install ./ibm-iaccess-1.1.0.15-1.0.ppc64el.deb
```

Installation
------------

Install py-systems-i.
```python
pip install py-systems-i
```
