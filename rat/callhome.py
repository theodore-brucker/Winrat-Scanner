import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Set the port number
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send a message to the server
client_socket.sendall(b'Hello, server')

# Receive data from the server
data = client_socket.recv(1024)

# Close the socket
client_socket.close()