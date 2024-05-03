import socket
import threading

TARGET_ADDRESS = ("localhost", 8080)
CLIENTS_TO_CREATE = 5


def start_client(i):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Client {i} is connecting to server at: {TARGET_ADDRESS}")
    client_socket.connect(TARGET_ADDRESS)

    # print("Sending data to server")
    # client_socket.send(f"Hello from client No.{i}".encode())


def main():
    threads = []
    for i in range(CLIENTS_TO_CREATE):
        client_thread = threading.Thread(target=start_client, args=(i,))
        threads.append(client_thread)

    for client_thread in threads:
        client_thread.start()

    for client_thread in threads:
        client_thread.join()


main()
