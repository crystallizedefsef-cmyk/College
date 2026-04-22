import socket

# Создаем UPD-сокет (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Привязываем к адресу и порту
server_socket.bind(('127.0.0.1', 8889))
print("UDP сервер запущен на порту 127.0.0.1:8889")

while True:
    #Данные и адрес отправителя
    data, client_addr = server_socket.recvfrom(1024)
    print(f"Получено от {client_addr}: {data.decode('utf-8')}")
    
    # Отправляем эхо обратно 
    server_socket.sendto(data, client_addr)