from dataclasses import dataclass
import socket
import threading

HOST = "0.0.0.0"
PORT = 8000
BUFFER_SIZE = 1024
NO_DATA = b""

lock = threading.Lock()


@dataclass
class Client:
    socket: socket.socket
    address: tuple[str, int]

    def __str__(self) -> str:
        return f"[{self.address[0]}:{self.address[1]}]"


class TcpServer:
    def __init__(self, host: str, port: int, backlog: int = 0):
        self._host = host
        self._port = port
        self._backlog = backlog
        self._listening_socket: socket.socket = None
        self._client_sockets: list[Client] = []

    @property
    def address(self) -> tuple:
        return self._host, self._port

    def start(self):
        if not self._listening_socket:
            self._initialize_listening_socket()

        print("Starting to wait for client connections...")
        while True:
            client = Client(*self._listening_socket.accept())
            client_thread = threading.Thread(target=self._handle_client, args=(client,))
            client_thread.start()

    def _initialize_listening_socket(self):
        print(f"Initializing TCP listening socket to {self.address}")
        self._listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._listening_socket.bind(self.address)
        self._listening_socket.listen(self._backlog)

    def _handle_client(self, client: Client):
        self._add_client(client)
        try:
            self._receive_messages(client)
        except Exception as error:
            print(f"[!] Client {client} has encountered an error: {error}")
        finally:
            self._remove_client(client)

    def _add_client(self, client: Client):
        with lock:
            print(f"[+] Adding client {client} to the socket list")
            self._client_sockets.append(client)

    def _remove_client(self, client: Client):
        print(f"[-] Closing socket for client: {client}")
        client.socket.close()

        with lock:
            print(f"[-] Removing client {client} from the socket list")
            self._client_sockets.remove(client)

    @staticmethod
    def _receive_messages(client: Client):
        print(f"Starting to receive messages from client: {client}")

        while True:
            data = client.socket.recv(BUFFER_SIZE)
            if data == NO_DATA:
                print(f"Received empty data from {client}. Assuming he has disconnected...")
                break
            print(f"{client} sent: {data.decode()}")


if __name__ == "__main__":
    server = TcpServer(HOST, PORT)
    server.start()
