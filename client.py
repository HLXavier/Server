import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

PORT = 5050

# ipconfig / IPv4
host_name = socket.gethostname()
SERVER = socket.gethostbyname(host_name)

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send_text = input('What message do you whant to send: ')
send(send_text)
send(DISCONNECT_MESSAGE)