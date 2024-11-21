import socket
import time

def start_ping_client(host='127.0.0.1', port=12345, initial_spin=0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to Pong server at {host}:{port}") 
        spin = initial_spin

        while spin < 10: # Perform Ping-Pong until spin is 10
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
                time.sleep(1) # Wait for 1 second before the next iteration
            except ValueError:
                print("Error: Invalid response from server")
                break

if __name__ == "__main__":
    start_ping_client() 