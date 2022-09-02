import os
import paramiko
import ntpath
import logging

logging.basicConfig(level=logging.INFO)


class SFTPClient(object):
    """
    Class for SSH client
    """

    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_host_keys(
            os.path.expanduser(os.path.join("~", ".ssh", "known_hosts"))
        )
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ISERIE_HOST = os.getenv("ISERIE_HOST")
        self.ISERIE_USER = os.getenv("ISERIE_USER")
        self.ISERIE_PASSWORD = os.getenv("ISERIE_PASSWORD")
        self.SFTP_PORT = os.getenv("SFTP_PORT")
        self.SFTP_REMOTE_PATH = os.getenv("SFTP_REMOTE_PATH")

    def connect(self):
        try:
            self.ssh_client.connect(
                hostname=self.ISERIE_HOST,
                username=self.ISERIE_USER,
                password=self.ISERIE_PASSWORD,
                port=self.SFTP_PORT,
            )
            msg = "{}: {}".format(self.ISERIE_HOST, "CONNECTED")
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
        sftp.chdir(self.SFTP_REMOTE_PATH)
        filenames = []
        for filename in sftp.listdir_attr():
            filenames.append("{}".format(filename))
        sftp.close()

        return filenames

    def upload(self, path_file):
        local_file_path = path_file
        remote_path = "{}{}".format(self.SFTP_REMOTE_PATH, ntpath.basename(path_file))
        ftp_client = self.ssh_client.open_sftp()
        ftp_client.put(local_file_path, remote_path)
        ftp_client.close()

        msg = "TRANSFERRED: {}".format(remote_path)
        logging.info(msg)
