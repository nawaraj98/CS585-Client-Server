import socket

def receive_file_from_server(sock):
    # Read the filename until a newline character is encountered
    filename = b''
    while True:
        char = sock.recv(1)
        if char == b'\n':
            break
        filename += char
    filename = filename.decode('utf-8').strip()  # Decode and remove any leading/trailing whitespace
    
    # Open a file with the received filename for writing binary data
    with open(filename, 'wb') as file:
        while True:
            data = sock.recv(1024)  # Read data in chunks 
            if not data:
                break  # Connection closed by the server
            
            file.write(data)

def connect_to_server(server_host, server_port):
    for connection_number in range(num_connections):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_host, server_port))
            print(f"Connected to {server_host}:{server_port}")

            receive_file_from_server(client_socket)  # Receive and save the file from the server

        
        print(f"Disconnected from the server. Reconnecting...")

server_host = '127.0.0.1'
server_port = 2002
num_connections = 15  # Number of times to connect to the server

connect_to_server(server_host, server_port)
