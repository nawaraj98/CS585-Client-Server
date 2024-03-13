import socket

def send_file_to_client(sock, filename):
    # Send the filename followed by a newline character
    sock.sendall((filename + '\n').encode('utf-8'))

    # Open the file in binary mode and send its contents
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)  # Read data in chunks
            if not data:
                break  # End of file
            
            sock.sendall(data)

server_host = '127.0.0.1'
server_port = 2002

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind to the port
    server_socket.bind((server_host, server_port))

    # Put the socket into listening mode
    server_socket.listen()

    print(f"Server is listening on {server_host}:{server_port}")

    # a forever loop until client wants to exit
    while True:
        # Establish connection with client
        client_socket, addr = server_socket.accept()

        print(f"Got connection from {addr}")

        # Call our function to send a file to the client
        send_file_to_client(client_socket, 'my_test_file.txt')

        # Close the connection with the client
        client_socket.close()
