import os
import unittest
from pathlib import Path
from pyiaccess.engine import set_env, create_sftp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_env = os.path.join(BASE_DIR, ".back.env")
set_env(path_env)


class TestSFTPClient(unittest.TestCase):
    def setUp(self):
        hostname = os.getenv("SFTP_HOST", None)
        username = os.getenv("SFTP_USER", None)
        password = os.getenv("SFTP_PASSWORD", None)
        port = os.getenv("SFTP_PORT", None)
        remote_path = os.getenv("SFTP_REMOTE_PATH", None)

        if not hostname and username and password:
            raise Exception("Sorry, Undefined environment variables.")

        self.path_file = os.path.join(BASE_DIR, "Clases.csv")

        self.engine = create_sftp(
            hostname=hostname,
            username=username,
            password=password,
            port=port,
            remote_path=remote_path,
        )

    def test_is_file(self):
        self.assertEqual(Path(self.path_file).is_file(), True)

    def test_upload_file(self):
        self.engine.connect()
        self.engine.upload(self.path_file)


if __name__ == "__main__":
    unittest.main()
