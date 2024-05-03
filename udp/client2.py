import socket

TARGET_HOST = "localhost"
TARGET_PORT = 60953
BUFFER_SIZE = 1024


def main():
    print("Creating TCP client socket...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Sending data to ({TARGET_HOST}, {TARGET_PORT})...")
    client_socket.sendto(b"Hello World From Client2", (TARGET_HOST, TARGET_PORT))

    data = client_socket.recvfrom(BUFFER_SIZE)
    print(data)


if __name__ == "__main__":
    main()
