import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 8000
EMPTY_DATA = ""
BUFFER_SIZE = 1024


def receive_messages(client_socket: socket.socket, client_address: tuple):
    while True:
        data = client_socket.recv(BUFFER_SIZE).decode()
        if data == EMPTY_DATA:
            print(f"Received empty data from {client_address}. Assuming he has disconnected...")
            break
        print(f"{client_address} Sent: {data}")


def handle_client(client_socket: socket.socket, client_address: tuple):
    print(f"Starting to handle client {client_address}")

    try:
        receive_messages(client_socket, client_address)
    except Exception as error:
        print(f"Client {client_address} has encountered an error while receiving messages: {error}")
    finally:
        print("Closing connection...")
        client_socket.close()


def main():
    print("Creating TCP server socket...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Binding server socket to ({HOST}, {PORT})...")
    server_socket.bind((HOST, PORT))

    print("Starting to listen (no queue backlog limit is set)")
    server_socket.listen()

    print("Starting to accept connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    main()
