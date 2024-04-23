import socket
import threading
import sys
import os

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(request)

    with open("index.html", "r") as f:
        response = f.read()

    http_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + response
    client_socket.sendall(http_response.encode())
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started at {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")

        handle_client(client_socket)

if __name__ == "__main__":
    main()
