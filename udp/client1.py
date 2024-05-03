import socket
import time

TARGET_HOST = "localhost"
TARGET_PORT = 8000
BUFFER_SIZE = 1024


def main():
    print("Creating TCP client socket...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Sending data to ({TARGET_HOST}, {TARGET_PORT})...")
    client_socket.sendto(b"Hello World From Client1 (1)", (TARGET_HOST, TARGET_PORT))

    print("Waiting to receive data back...")
    data, address = client_socket.recvfrom(BUFFER_SIZE)
    data = data.decode()
    print(f"{address} sent: {data}")

    print(f"Sending data to ({TARGET_HOST}, {TARGET_PORT})...")
    client_socket.sendto(b"Hello World From Client1 (2)", (TARGET_HOST, TARGET_PORT))

    print("Sleeping for 100 seconds")
    time.sleep(100)


if __name__ == "__main__":
    main()
