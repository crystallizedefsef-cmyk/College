import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 8889)

message = "Hello, UDP server!"
client_socket.sendto(message.encode('utf-8'), server_addr)

# Получаем ответ
data, _ = client_socket.recvfrom(1024)
print(f"Ответ от сервера: {data.decode('utf-8')}")

client_socket.close()