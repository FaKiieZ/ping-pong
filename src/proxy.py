import socket
import time
 
def start_proxy_server(proxy_host, proxy_port, pong_host, pong_port):
    print(f"Proxy server is starting on {proxy_host}:{proxy_port}, forwarding to Pong at {pong_host}:{pong_port}...")
 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
            proxy_socket.bind((proxy_host, proxy_port))
            proxy_socket.settimeout(1.0)  # Set a short timeout for accept()
            proxy_socket.listen(1)

            isWaiting = False

            print(f"Proxy server is listening on {proxy_host}:{proxy_port}...")
 
            while True:
                # Accept connections with a timeout to allow interruption
                try:
                    conn, addr = proxy_socket.accept()
                    isWaiting = False
                    print(f"Ping connected from {addr}")
 
                    with conn:
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            print(f"Proxy received from Ping: {data.decode()}")
 
                            # Forward data to Pong
                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as pong_socket:
                                pong_socket.connect((pong_host, pong_port))
                                pong_socket.sendall(data)
                                print(f"Proxy forwarded to Pong: {data.decode()}")
 
                                # Get response from Pong
                                pong_response = pong_socket.recv(1024)
                                print(f"Proxy received from Pong: {pong_response.decode()}")
 
                                # Send response back to Ping
                                conn.sendall(pong_response)
                                print(f"Proxy sent back to Ping: {pong_response.decode()}")
 
                except socket.timeout:
                    if not isWaiting:
                        isWaiting = True
                        print("Waiting for new connections... Cancel with Ctrl+C\n")
                    pass  # Periodically check for interrupts while waiting for connections
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt received. Shutting down proxy server...")
                    break
                except Exception as e:
                    print(f"An unexpected error occurred in Proxy: {e}")
    except KeyboardInterrupt:
        print("\nProxy server was terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
if __name__ == "__main__":
    PROXY_IP = input("Please input the proxy server ip address (empty equals to default: 127.0.0.1): ") or '127.0.0.1'
    try:
        PROXY_PORT = int(input("Please input the proxy server port (empty equals to default: 5000): ") or '5000')
    except ValueError:
        print("Error: Invalid port number, using default value: 5000")
        PROXY_PORT = 5000
 
    PONG_IP = input("Please input the pong server ip address (empty equals to default: 127.0.0.1): ") or '127.0.0.1'
    try:
        PONG_PORT = int(input("Please input the pong server port (empty equals to default: 12345): ") or '12345')
    except ValueError:
        print("Error: Invalid port number, using default value: 12345")
        PONG_PORT = 12345
 
    start_proxy_server(PROXY_IP, PROXY_PORT, PONG_IP, PONG_PORT)