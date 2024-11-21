import socket
import time
 
def start_pong_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Pong server is listening on {host}:{port}...")
 
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    try:
                        number = int(data.decode())
                        print(f"Received: {number}")
                        response = number + 1

                        time.sleep(1) # Wait for 1 second before the next iteration
                        conn.sendall(str(response).encode())
                        print(f"Sent: {response}")
                    except ValueError:
                        conn.sendall(b"Error: Invalid number")
 
if __name__ == "__main__":
    start_pong_server()