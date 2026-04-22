import socket

# 1. Создаем TCP сокет 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Подключаемся к серверу по адрресу и порту
client_socket.connect(('127.0.0.1', 8888))

# 3. Отправляем сообщение (строку преобразуем в байты)
message = "Hello, server!"
client_socket.send(message.encode('utf-8'))

print("Сообщение отправлено!")

# 4. Закрываем сокет
client_socket.close()