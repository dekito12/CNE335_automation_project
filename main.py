import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, rsa_key_file):
        self.server_ip = server_ip
        self.rsa_key_file = rsa_key_file
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.server_ip, username='ubuntu', key_filename=self.rsa_key_file)

    def ping(self):
        response = os.system("ping -c 5 " + self.server_ip)
        return response == 0


def print_program_info():
    print("Server Automator v0.1 by Dekow")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    my_server_ip = "35.161.200.181"
    my_rsa_key_file = "/Users/dekowali/.ssh/id_rsa"
    server = Server(my_server_ip, my_rsa_key_file)
    if server.ping():
        print("Server is reachable.")
    else:
        print("Server is not reachable.")
    server.disconnect()
