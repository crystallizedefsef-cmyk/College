import socket
import threading

def handle_client(client_socket, client_address):
    """Функция обработки одного клиента """
    print(f"Новый клиент:  {client_address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                # Клиент закрыл соединение
                break
            print(f"Получено от {client_address}: {data.decode('utf-8')}")
            # отправляем эхо обратно
            client_socket.sendall(data)
    except ConnectionResetError:
        print(f"Клиент {client_address} оборвал соединение")
    finally:
        client_socket.close()
        print(f"Соединение с {client_address} закрыто")

# Основной серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(5)
print("TCP-сервер запущен на 127.0.0.1:8888, ожидаем клиентов.")

while True:
    client_sock, client_addr = server_socket.accept()
    # Создаем новый поток для клиента
    thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
    thread.start()
    print(f"Активных потоков: {threading.active_count() - 1}") # - главный поток