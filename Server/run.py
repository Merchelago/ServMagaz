import socket
import sys
from math import sin, exp, tan, atan
HOST = "127.0.0.1"
PORT = 5556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
        s.listen(10)
        print('Сервер запущен и ожидает подключений...')
        conn, addr = s.accept()
        while True:
            conn, addr = s.accept()
            print('Подключен клиент:', addr)

            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print('Клиент отключился')
                        break
                    conn.sendall(data)
    finally:
        s.close()  # Закрытие сокета для освобождения ресурсов
