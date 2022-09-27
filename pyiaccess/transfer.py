import os
import paramiko
import ntpath
import logging

logging.basicConfig(level=logging.INFO)


class SFTPClient(object):
    """
    Class for SSH client
    """

    def __init__(self, **kwargs):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_host_keys(
            os.path.expanduser(os.path.join("~", ".ssh", "known_hosts"))
        )
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.SFTP_HOST = kwargs.get("hostname", None)
        print(self.SFTP_HOST)
        self.SFTP_USER = kwargs.get("username", None)
        self.SFTP_PASSWORD = kwargs.get("password", None)
        self.SFTP_PORT = kwargs.get("port", 22)
        self.SFTP_REMOTE_PATH = kwargs.get("remote_path", None)

    def connect(self):
        try:
            self.ssh_client.connect(
                hostname=self.SFTP_HOST,
                username=self.SFTP_USER,
                password=self.SFTP_PASSWORD,
                port=self.SFTP_PORT,
            )
            msg = f"{self.SFTP_HOST}: CONNECTED"
            logging.info(msg)
        except paramiko.AuthenticationException as exc:
            logging.error("Authentication Failed")
            raise exc
        except paramiko.SSHException as exc:
            logging.error("SSH Error")
            raise exc
        except Exception as exc:
            logging.error(f"Unknown Error: {exc}")
            raise str(exc)

    def list_files(self):
        sftp = self.ssh_client.open_sftp()
        sftp.chdir(self.SFTP_REMOTE_PATH)
        filenames = []
        for filename in sftp.listdir_attr():
            filenames.append(f"{filename}")
        sftp.close()

        return filenames

    def upload(self, path_file):
        local_file_path = path_file
        remote_path = f"{self.SFTP_REMOTE_PATH}{ntpath.basename(path_file)}"
        ftp_client = self.ssh_client.open_sftp()
        ftp_client.put(local_file_path, remote_path)
        ftp_client.close()

        msg = f"TRANSFERRED: {remote_path}"
        logging.info(msg)
