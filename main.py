from Server import Server


def print_program_info():
    print("Server Automator v0.1 by Dekow")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    my_server_ip = "35.161.200.181"
    my_rsa_key_file = "/Users/dekowali/.ssh/id_rsa"
    username = "ubuntu"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))
