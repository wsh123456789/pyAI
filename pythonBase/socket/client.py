import socket
sock_client = socket.socket()

sock_client.connect(('127.0.0.1', 8080))
sock_client.send("你好".encode('utf-8'))

recv_data = sock_client.recv(1024)
print(recv_data.decode('utf-8'))

sock_client.close()
