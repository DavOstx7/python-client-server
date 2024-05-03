import socket

TARGET_HOST = "localhost"
TARGET_PORT = 8000


class TcpClient:
    def __init__(self, target_ip: str, target_port: int):
        self._target_ip = target_ip
        self._target_port = target_port
        self._socket: socket.socket = None

    @property
    def target_address(self) -> tuple:
        return self._target_ip, self._target_port

    def start(self):
        if not self._socket:
            self._initialize_socket()

        try:
            self._send_user_input()
        except Exception as error:
            print(f"An error has occurred: {error}")
        finally:
            print(f"Closing socket")
            self._socket.close()

    def _initialize_socket(self):
        print(f"Initializing TCP socket connection to {self.target_address}")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(self.target_address)

    def _send_user_input(self):
        print("Starting to receive input to send to the server. Use 'exit' or 'break' to stop")
        while True:
            data = input("Enter your data: ")
            if data.lower() == "exit" or data.lower() == "break":
                break
            self._socket.send(data.encode())


if __name__ == "__main__":
    client = TcpClient(TARGET_HOST, TARGET_PORT)
    client.start()
