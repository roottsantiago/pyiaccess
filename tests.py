import os
import unittest
from pathlib import Path
from pyiaccess.manage import set_env
from pyiaccess.db import ConnexionClient
from pyiaccess.transfer import SFTPClient

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_env = os.path.join(BASE_DIR, ".back.env")
set_env(path_env)


class TestDBClient(unittest.TestCase):
    def setUp(self):
        self.cnn = ConnexionClient()

    def test_connexion(self):
        message = "Given object is not instance of ConnexionClient."
        self.assertIsInstance(self.cnn, ConnexionClient, message)

    def test_sql_selected_all(self):
        sql = """SELECT * FROM TSANTIAGO.NF01"""
        data = self.cnn.execute(sql)
        columns = [column[0] for column in data.description]

        results = []
        for row in data:
            results.append(dict(zip(columns, row)))

        message = "The query as a result must contain data."
        self.assertTrue(results, message)

    def test_sql_select(self):
        sql = """SELECT * FROM TSANTIAGO.NF01
        WHERE NEMPL=?
        """
        data = self.cnn.execute(sql, params=["215"])
        columns = [column[0] for column in data.description]

        results = []
        for row in data:
            results.append(dict(zip(columns, row)))

        message = "La consulta como resultado no debe obtener datos"
        self.assertFalse(results, message)

    def test_sql_insert(self):
        sql = """
        INSERT INTO TSANTIAGO.TB_EMPLOYEE_UPD(CCIA, COCIA, NEMPL, CCOST) 
        VALUES (?,?,?,?)
        """
        params = [1, "test2", "1", "0"]
        data = self.cnn.execute(sql, params)

        message = "First value and second value are not equal."
        self.assertEqual(data.rowcount, 1, message)

    def test_sql_update(self):
        sql = """
        UPDATE TSANTIAGO.TB_EMPLOYEE_UPD
        SET COCIA = ?
        WHERE NEMPL=?
        """
        params = ["demo", "1"]
        data = self.cnn.execute(sql, params)

        message = "Given object is not instance of data.rowcount"
        self.assertIsInstance(data.rowcount, int, message)


class TestSFTPClient(unittest.TestCase):
    def setUp(self):
        self.path_file = os.path.join(BASE_DIR, "Clases.csv")

    def test_is_file(self):
        self.assertEqual(Path(self.path_file).is_file(), True)

    def test_upload_file(self):
        sftp = SFTPClient()
        sftp.connect()
        sftp.upload(self.path_file)


if __name__ == "__main__":
    unittest.main()
