# This is the template code for the CNE335 Final Project
# Dekow
# CNE 335 Fall
import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        response = os.system("ping -c 5 " + self.server_ip)
        return response == 0

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Dekow")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("35.161.200.181")  # create a server object
    if server.ping():
        print(server.ping())
    else:
        print("Server is not responding.")
