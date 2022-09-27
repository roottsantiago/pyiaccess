# -*- coding: utf-8 -*-
import os
import pyodbc
from pyiaccess.helpers.common import generic_error


class IBMClient(object):
    """
    Base class for database connection.
    """

    _DRIVER = "IBM i Access ODBC Driver"

    def __init__(self, **kwargs):
        self._IBMI_HOST = kwargs.get("hostname", None)
        self._IBMI_DSN = kwargs.get("dsn", None)
        self._IBMI_USER = kwargs.get("username", None)
        self._IBMI_PASSWORD = kwargs.get("password", None)
        self._IBMI_PORT = kwargs.get("port", None)

        self.conn_str = (
            f"SYSTEM={self._IBMI_HOST};db2:DSN={self._IBMI_DSN};UID={self._IBMI_USER};"
        )
        if self._IBMI_PORT:
            port = f"PORT={self._IBMI_PORT};"
            self.conn_str += port
        self.conn_str += f"PWD={self._IBMI_PASSWORD};DRIVER={self._DRIVER};"

    def connect(self):
        self._cnn = pyodbc.connect(self.conn_str)
        self._cnn.autocommit = True

    def close(self):
        """
        Closes the cursor.

        A ProgrammingError exception will be raised
        if any operation is attempted with the cursor.
        """
        self._cnn.close()

    @generic_error
    def fetch_all(self, query):
        """
        Returns a list of all remaining rows.

        Since this reads all rows into memory, it should not be used if
        there are a lot of rows. Consider iterating over the rows instead.
        However, it is useful for freeing up a Cursor so you can perform
        a second query before processing the resulting rows.
        """
        cursor = self._cnn.cursor()
        data = cursor.execute(query)
        data = data.fetchall()
        cursor.close()
        return data

    @generic_error
    def execute(self, query, params=[]):
        """
        Prepares and executes SQL.

        The optional parameters may be passed as a sequence,
        as specified by the DB API, or as individual values.
        """
        cursor = self._cnn.cursor()
        data = cursor.execute(query) if not params else cursor.execute(query, params)
        cursor.commit()
        return data

    @generic_error
    def execute_many(self, query, params):
        """
        Executes the same SQL statement for each set of parameters.
        seq_of_parameters is a sequence of sequences.
        """
        try:
            cursor = self._cnn.cursor()
            cursor.executemany(query, params)
        except pyodbc.DatabaseError as error:
            cursor.rollback()
            print(error)
        else:
            cursor.commit()
        return True

    @generic_error
    def call(self, usp_name, resultset=False):
        cursor = self._cnn.cursor()
        cursor.execute(usp_name)

        response = None
        if resultset:
            response = cursor.fetchone()
            issuccess = response[0]
            cosqlstate = response[1]
            cosqlcode = response[2]
            msgtext = response[3]

            if not bool(issuccess):
                error = {
                    "cosqlstate": [
                        cosqlstate,
                    ],
                    "cosqlcode": [
                        cosqlcode,
                    ],
                    "detail": [
                        msgtext,
                    ],
                }
                raise Exception(error)

        return response
