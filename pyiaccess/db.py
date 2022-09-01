# -*- coding: utf-8 -*-
import os
import pyodbc
from pyiaccess.helpers.common import generic_error


class ConnexionClient(object):
    """
    Base class for database connection.
    """

    _DRIVER = "IBM i Access ODBC Driver"

    def __init__(self):
        conn = "SYSTEM={};db2:DSN={};UID={};PWD={};DRIVER={};".format(
            os.getenv("ISERIE_HOST"),
            os.getenv("ISERIE_DSN"),
            os.getenv("ISERIE_USER"),
            os.getenv("ISERIE_PASSWORD"),
            self._DRIVER,
        )
        self._cnn = pyodbc.connect(conn)
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
    def call(self, usp_name, resultset):
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
