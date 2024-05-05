import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
print("Server listening on port 9999")

client_socket, addr = server.accept()
print(f"Accepted connection from {addr}")

while True:
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message from {addr}: {data}")

        client_socket.send(data.encode())

        response = input("you: ")
        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error: {e}")
        break

print(f"Connection from {addr} closed.")
client_socket.close()
