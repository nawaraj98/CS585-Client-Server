This project involves a client-server architecture for file transfer. The client side, written in Python, connects to a server specified by an IP address and port. 
It iteratively connects to the server a predetermined number of times and receives a file from it. The server, also written in Python, listens on a specified IP address and port. 
When a client connects, it sends a file ('my_test_file.txt' in this case) to the client. 
The expected result is a successful file transfer from the server to the client, with the client reconnecting multiple times as specified.
