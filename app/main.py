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
    client_socket, address_info = server_socket.accept()

    with client_socket:
        # status = "HTTP/1.1 200 OK\r\n\r\n"
        request = client_socket.recv(1024).decode("utf-8")
        request = request.split("\r\n")
        # header_path = request.split("\r\n")[0].split(" ")[1]
        path=request[0].split()[1].split("/")
        # if len(path) == 2:
        userAgent = request[2].split()[-1]
        if path[1] == "":
            response=f"HTTP/1.1 200 OK\r\n\r\n"
            # status = "HTTP/1.1 200 OK\r\n\r\n"
            # status = status.encode("utf-8")
            # client_socket.send(status)
        elif path[1] == "echo":
             text = "/".join(path[2:])
             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(text)}\r\n\r\n{text}"
        elif path[1] == "user-agent":
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(userAgent)}\r\n\r\n{userAgent}"
            
        else:
            response = "HTTP/1.1 404 Not Found response\r\n\r\n"
            # status = status.encode("utf-8")
        client_socket.send(response.encode("utf-8"))


if __name__ == "__main__":
    main()
 