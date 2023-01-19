import socket

def check_client(ip_address):
    home_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    home_socket.settimeout(5)
    result = home_socket.connect_ex((ip_address, 22))
    if result == 0:
        print(f'{ip_address} is online')
        return True
    else:
        print(f'{ip_address} is offline')
        return False

# Example usage
check_client("10.3.32.1")