# server.py
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('0.0.0.0', 4444))  # Listen on all interfaces
listener.listen(1)
print("[*] Waiting for connection...")

client_socket, addr = listener.accept()
print(f"[+] Connection received from {addr}")

while True:
    command = input("Shell> ")
    if command.lower() in ["exit", "quit"]:
        client_socket.send(command.encode())
        break

    client_socket.send(command.encode())
    output = client_socket.recv(4096).decode()
    print(output)

client_socket.close()
listener.close()
