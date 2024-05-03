import socket
import threading
import time

BINDING_ADDRESS = ("0.0.0.0", 8080)
LISTEN_BACKLOG = 2
SLEEP_TIME = 10


def handle_client(client_socket, client_address):
    print(f"Handling client: {client_address}")

    data = client_socket.recv(1024).decode()
    print(f"{client_address} sent: {data}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Binding server socket to: {BINDING_ADDRESS}")
    server_socket.bind(BINDING_ADDRESS)

    print(f"Listening backlog: {LISTEN_BACKLOG}")
    server_socket.listen(LISTEN_BACKLOG)

    print(f"Sleeping for: {SLEEP_TIME}")
    time.sleep(SLEEP_TIME)

    print("Starting to accept connections!")
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


main()
