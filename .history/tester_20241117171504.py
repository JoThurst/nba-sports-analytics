import socket

host = "73.159.20.15"
port = 5432

try:
    with socket.create_connection((host, port), timeout=5):
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
