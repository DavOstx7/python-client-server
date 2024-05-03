import socket

HOST = "0.0.0.0"
PORT = 8000
BUFFER_SIZE = 1024


def main():
    print("Creating UDP server socket...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Binding socket to ({HOST}, {PORT})...")
    server_socket.bind((HOST, PORT))

    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        data = data.decode()
        print(f"{client_address} sent: {data}")

        server_socket.sendto(b"Hello World from server", client_address)
        # If we have a complicated logic, we might want to use a thread-pool to not block the loop from continuing


if __name__ == "__main__":
    main()
