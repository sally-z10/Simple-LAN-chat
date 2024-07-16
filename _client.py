import socket

# Constants
PORT = 49999 #check port numbers
DISCONNECT_MSG = "disconnect"
SERVER = "192.168.42.218"
ADDR = (SERVER, PORT)

# connect client to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode('utf-8')
    msg_length = len(message) # check message length to check if it matches the defualt message length we set in server.py (64)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (64 - len(send_length)) # padding the message with blank spaces to make sure it is the correct length (64)

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))


send_message("Hello !")
input()
send_message("Zuko here !!")
input()
send_message(DISCONNECT_MSG)
