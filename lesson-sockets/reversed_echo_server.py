"""
Сокеты

Основные функции:
socket - создает новый сокет и вощращает файловый дескриптор
send   - отправить (записать) данные в сокет
        send - низкуровневый метод, возвращает количество отправленных байт
        sendall - высокоуровневый метод Python, если была ошибка, то исключение
recv   - получить (прочитать) данные из сокета
close  - закрыть соединение

Серверный сокет:
bind   - связывает сокет с IP-адресом и портом
listen - объявить о желании принимать соединение
accept - принять запрос на установку соединения

Клиентский сокет:
connect - установить соединени

"""


from datetime import datetime
import socket
import threading

def log(msg):
    print(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}')

def readall(sock, chunk_size=1024):
    """Возвращает все данные отправленные в сокет"""
    buffer = b''
    finished = False

    while not finished:
        chunk = sock.recv(chunk_size)
        buffer += chunk

        if not chunk or len(chunk) < chunk_size:
            finished = True

    return buffer

def connection_handler(conn, addr):
    """Обработчик входящего соединения"""
    log(f'New connection: {addr}')
    data = data.readall(conn).decode()
    data = data[::-1]
    conn.sendall(data.encode())
    conn.close()

def make_server(host='localhost', port=8000, backlog=2):
    """
    Создает сервер и запускает его на прослушку входящих соединений
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # socket.SOCK_DGRAM - нет гарантий
        # SOCK_STREAM контролирует поток, гарнтия, что данные дойдут
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(backlog) # backlog размер очереди ожидающих соединение

        log('The server is running and waiting for incoming request...')
        log(f'-> Adress: {host}:{port}')

        while 1:
            conn, addr = sock.accept()
            thread = threading.Thread(
                target=connection_handler,
                args=(conn, addr),
                daemon=True
            )
            thread.run()

def make_client(host='localhost', port=8000):
    """Создает клиент"""
    while 1:
        message = input('Enter message: ')

        if message == r'\b':
            break

        if message:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.connect((host, port))
                    sock.sendall(message.encode())
                    answer = sock.readall(sock).decode()
                    print(f'-> {answer}')

                except socket.error as err:
                    print(err)
                    break

    print('Good bye!')
