import socket
import threading

# Constants
PORT = 49999 #check port numbers
SRV_ADDR = socket.gethostbyname(socket.gethostname()) #local ipv4 address of the computer that will acct as a server
ADDR = (SRV_ADDR, PORT)
DISCONNECT_MSG = "disconnect"

# making a socket for the server and binding it to it
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def startserver():
    print("Server Starting...")
    server.listen()
    print(f"Listening on {SRV_ADDR}...")

    while True:
        client , cl_addr = server.accept()
        thread = threading.Thread(target=handle_client_requests, args=(client , cl_addr))
        thread.start()

def handle_client_requests(client , cl_addr):
    print(f"New Connection: {cl_addr} is connected !!")

    connection_status = True
    while connection_status:
        msg_length = client.recv(64).decode('utf-8') #fix a certain length and format for the messages
        if msg_length: # to evade error when first connecting
            msg_length = int(msg_length)
            message = client.recv(msg_length).decode('utf-8')
            
            #to disconnect check for disconnect message
            if message == DISCONNECT_MSG:
                connection_status = False

            print(f"~{cl_addr}: {message}")
            client.send("[Message Received !]".encode('utf-8'))

    print(f"-- {cl_addr} is DISCONNECTED --")
    client.close()

startserver()