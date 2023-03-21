import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip, key_file, username, upgrade_command):
        self.server_ip = server_ip
        self.username = username
        self.command = upgrade_command
        self.key_file = key_file

    def ping(self):
        result = os.system("ping -n 5 %s" % self.server_ip)
        return result

    def ssh_command(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file(self.key_file)
        ssh_client.connect(hostname=self.server_ip, username=self.username, pkey=k)

        stdin, stdout, stderr = ssh_client.exec_command(self.command)

        for line in stdout.read().splitlines():
            print(line)

        ssh_client.close()

# create a Server instance with the required arguments
server = Server('35.161.200.181', '/Users/dekowali/.ssh/id_rsa', 'ubuntu', 'ls -l /tmp')

# ping the server to check connectivity
ping_result = server.ping()
if ping_result == 0:
    print('Server is reachable.')
else:
    print('Server is not reachable.')

# execute the command on the server using SSH
print('Executing command on the server...')
server.ssh_command()
print('Command execution completed.')
