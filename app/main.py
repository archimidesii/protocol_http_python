import socket
import threading

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        client_socket, adress_info = server_socket.accept()  # wait for client
        threading.Thread(
            target=handleRequest, args=(client_socket, adress_info)
        ).start()

def handleRequest(client_socket, address_info):
    with client_socket:
        # status = "HTTP/1.1 200 OK\r\n\r\n"
        request = client_socket.recv(1024).decode("utf-8")
        request = request.split("\r\n")
        data_path = request[0].split()[1]
        if data_path == "/":
            status = "HTTP/1.1 200 OK\r\n\r\n"
        elif data_path.startswith("/echo"):
            random_string = data_path.split("/echo/")[1]
            status = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(random_string)}\r\n\r\n"
                f"{random_string}"
            )
        elif data_path.startswith("/user-agent"):
            user_agent_header = request[2]
            user_agent_data = user_agent_header.split("User-Agent: ")[1]
            status = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(user_agent_data)}\r\n\r\n"
                f"{user_agent_data}"
            )
        else:
            status = "HTTP/1.1 404 Not Found\r\n\r\n"
            # status = status.encode("utf-8")
        client_socket.send(status.encode())


if __name__ == "__main__":
    main()
 