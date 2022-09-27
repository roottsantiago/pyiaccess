import os
import unittest
from pyiaccess.engine import set_env, create_db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_env = os.path.join(BASE_DIR, ".back.env")
set_env(path_env)


class TestDBClient(unittest.TestCase):
    
    def setUp(self):
        hostname = os.getenv("IBMI_HOST", None)
        dsn = os.getenv("IBMI_DSN", None)
        username = os.getenv("IBMI_USER", None)
        password = os.getenv("IBMI_PASSWORD", None)
        port = os.getenv("IBMI_PORT", None)

        self.engine = create_db(
            hostname=hostname, dsn=dsn, username=username, password=password, port=port
        )
        self.engine.connect()

    def test_connexion(self):
        message = "Given object is not instance of ConnexionClient."
        self.assertIsInstance(self.engine, object, message)

    def test_sql_selected_all(self):
        sql = """SELECT * FROM TSANTIAGO.NF01"""
        data = self.engine.execute(sql)
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
        data = self.engine.execute(sql, params=["215"])
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
        data = self.engine.execute(sql, params)

        message = "First value and second value are not equal."
        self.assertEqual(data.rowcount, 1, message)

    def test_sql_update(self):
        sql = """
        UPDATE TSANTIAGO.TB_EMPLOYEE_UPD
        SET COCIA = ?
        WHERE NEMPL=?
        """
        params = ["demo", "1"]
        data = self.engine.execute(sql, params)

        message = "Given object is not instance of data.rowcount"
        self.assertIsInstance(data.rowcount, int, message)


if __name__ == "__main__":
    unittest.main()
