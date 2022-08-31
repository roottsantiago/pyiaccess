import os
import paramiko
import ntpath
import logging

logging.basicConfig(level=logging.INFO)


class SFTPClient(object):
    SFTP_HOST = os.getenv("ISERIE_HOST")
    SFTP_USER_NAME = os.getenv("ISERIE_USER")
    SFTP_PASSWORD = os.getenv("ISERIE_PASSWORD")
    SFTP_PORT = os.getenv("SFTP_PORT")
    SFTP_REMOTE_PATH = os.getenv("SFTP_REMOTE_PATH")

    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.ssh_client.connect(
                self.SFTP_HOST,
                username=self.SFTP_USER_NAME,
                password=self.SFTP_PASSWORD,
                port=self.SFTP_PORT,
            )
            msg = "{}: {}".format(self.SFTP_HOST, "CONNECTED")
            logging.info(msg)
        except paramiko.AuthenticationException as exc:
            print("Authentication Failed")
            raise exc
        except paramiko.SSHException as exc:
            print("SSH Error")
            raise exc
        except Exception as exc:
            print("Unknown Error: %s" % exc)
            raise str(exc)

    def list_files(self):
        sftp = self.ssh_client.open_sftp()
        sftp.chdir(self.SFTP_REMOTE_PATH_BASE)
        filenames = []
        for filename in sftp.listdir_attr():
            filenames.append("{}".format(filename))
        sftp.close()

        return filenames

    def upload(self, filename):
        local_file_path = filename
        remote_path = "{}{}".format(
            self.SFTP_REMOTE_PATH_BASE, ntpath.basename(filename)
        )

        ftp_client = self.ssh_client.open_sftp()
        ftp_client.put(local_file_path, remote_path)
        ftp_client.close()
        msg = "TRANSFERRED: {}".format(remote_path)
        logging.info(msg)
