import socket

TARGET_HOST = "localhost"
TARGET_PORT = 8000


def main():
    print("Creating TCP client socket...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Connecting to ({TARGET_HOST}, {TARGET_PORT})")
    client_socket.connect((TARGET_HOST, TARGET_PORT))

    while True:
        data = input("Enter data to send to server: ").encode()
        client_socket.send(data)


if __name__ == "__main__":
    main()
