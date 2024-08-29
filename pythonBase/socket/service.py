# 创建socket对象
import socket
socket_server = socket.socket()
# 绑定socket_server到指定ip和地址
host = "localhost"
port = 8080
socket_server.bind((host, port))
# 服务端开始监听端口 listen(backlog) backlog是最大连接量
socket_server.listen(5)
# 接收客户端连接，获得连接对象
conn, addr = socket_server.accept()
print('Connected by', addr)

# 接收客户端信息，要使用客户端和服务端的本次连接对象，而非socket_service对象
# recv接收的参数是缓冲区大小一般为1024
# recv返回值是一个字节数组也就是bytes对象,不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
data = conn.recv(1024).decode('utf-8')
print(data)
# 发送回复消息
msg = input("请输入返回给客户端的信息")
conn.send(msg.encode('utf-8'))
# 关闭连接
conn.close()
socket_server.close()
