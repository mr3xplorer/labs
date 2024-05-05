import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
print("Connected to server")

while True:
    message = input("Type your message: ")
    client.send(message.encode())
 
    response = client.recv(1024).decode()
    print("you: ", response)

    server_message = client.recv(1024).decode()
    print("Server: ", server_message)

