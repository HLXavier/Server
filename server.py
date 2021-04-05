import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

PORT = 5050

# ipconfig / IPv4
host_name = socket.gethostname()
SERVER = socket.gethostbyname(host_name)

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print('[CONNECTED] {0} just connected'.format(addr))
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        # when connecting the first message sent is a blank one
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print('[{0}] sad: {1}'.format(addr, msg))

            conn.send('Nice message!'.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print('[STARTING SERVER] ip: {}'.format(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print('[NEW CONNECTION] {0} users are connected now'.format(threading.activeCount() - 1))


start()
