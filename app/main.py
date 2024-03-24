# Uncomment this to pass the first stage
import socket

# GET /index.html HTTP/1.1
# Host: localhost:4221
# User-Agent: curl/7.64.1

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client
    client_socket, address = server_socket.accept()

    with client_socket:
        status = "HTTP/1.1 200 OK\r\n\r\n"
        request = client_socket.recv(1024)
        request = request.decode("utf-8")
        header_path = request.split("\r\n")[0].split(" ")[1]
        if header_path == "/":
            status = "HTTP/1.1 200 OK\r\n\r\n"
        else:
            status = "HTTP/1.1 404 Not Found\r\n\r\n"
        status = status.encode("utf-8")
        client_socket.send(status)


if __name__ == "__main__":
    main()
 