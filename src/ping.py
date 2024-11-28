import socket
import time

def start_ping_client(host, port, max_spin):
    print(f"Trying to connect to pong server at {host}:{port}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Successfully connected to pong server at {host}:{port}") 
            spin = 0

            while spin <= max_spin:  # Perform Ping-Pong until spin is max_spin
                try:
                    spin += 1
                    print(f"Sending: {spin}")
                    client_socket.sendall(str(spin).encode()) 
                    data = client_socket.recv(1024)

                    if not data:
                        print("Disconnected by server.")
                        break

                    print(f"Received: {data.decode()}")

                    try:
                        spin = int(data.decode())
                        time.sleep(1)  # Wait for 1 second before the next iteration
                    except ValueError:
                        print("Error: Invalid response from server")
                        break
                except socket.error as e:
                    print(f"Network error occurred: {e}")
                    break
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt received. Stopping client...")
                    break
    except KeyboardInterrupt:
        print("\nPing client was terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    SERVER_IP = input("Please input the pong server ip address (empty equals to default: 127.0.0.1): ") or '127.0.0.1'

    try:
        SERVER_PORT = int(input("Please input the pong server port (empty equals to default: 12345): ") or '12345')
    except ValueError:
        print("Error: Invalid port number, using default value: 12345")
        SERVER_PORT = 12345

    try:
        MAX_SPIN = int(input("Please input how many times a ping should be being sent to the pong server (empty equals to default: 10): ") or '10')
    except ValueError:
        print("Error: Invalid number, using default value: 10")
        MAX_SPIN = 10

    start_ping_client(SERVER_IP, SERVER_PORT, MAX_SPIN)
