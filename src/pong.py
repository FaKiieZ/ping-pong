import socket
import time

def start_pong_server(host, port):
    print(f"Pong server is trying to startup on {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.settimeout(1.0)  # Set a short timeout for accept()
            server_socket.listen(1)
            print(f"Pong server is listening on {host}:{port}...")
    
            while True:
                # Accept connections with a timeout to allow interruption
                try:
                    conn, addr = server_socket.accept()
                    print(f"Connected by {addr}")

                    with conn:
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            try:
                                number = int(data.decode())
                                print(f"Received: {number}")
                                response = number + 1

                                time.sleep(1)  # Wait for 1 second before the next iteration
                                conn.sendall(str(response).encode())
                                print(f"Sent: {response}")
                            except ValueError:
                                conn.sendall(b"Error: Invalid number")
                except socket.timeout:
                    pass  # Periodically check for interrupts while waiting for connections
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt received. Shutting down server...")
                    break
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nPong server was terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    SERVER_IP = input("Please input the pong server ip address (empty equals to default: 127.0.0.1): ") or '127.0.0.1'

    try:
        SERVER_PORT = int(input("Please input the pong server port (empty equals to default: 12345): ") or '12345')
    except ValueError:
        print("Error: Invalid port number, using default value: 12345")
        SERVER_PORT = 12345

    start_pong_server(SERVER_IP, SERVER_PORT)
