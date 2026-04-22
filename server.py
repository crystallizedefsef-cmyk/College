import socket

# 1. Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Привязываем сокет к адресу localhost и порту 8888
server_socket.bind(('127.0.0.1', 8888))

# 3. Сокет в режиме ожидания
# listen(1) - обработано будет только 1 соединение
server_socket.listen(1)
print("Сервер запущен на 127.0.0.1:8888, ожидаем подключения...")

# 4. Принимаем входящее соединение
client_socket, address = server_socket.accept()
print(f"Подключился клиент с адреса: {address}")

# 5. Получаем данные  от клиента (макс 1024 байта)
data = client_socket.recv(1024)
print(f"Получено сообщение: {data.decode('utf-8')}")  # Декодируем байты в строку

# 7. Закрываем соединения
client_socket.close()
server_socket.close()

# Чтобы окно консоли не закрылось сразу
input("\nEnter, чтобы выйти...")