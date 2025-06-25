import os
import sys
import socket
import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

HOST = "127.0.0.1"  
PORT = 12345

BLOCK_SIZE = 16
FLAG_PATH = "./flag.txt"

try:
    with open(FLAG_PATH, "rb") as f:
        FLAG = f.read().strip()
except FileNotFoundError:
    print(f"[!] {FLAG_PATH} missing — create the file with your real flag.")
    sys.exit(1)

KEY = os.urandom(16)
print(KEY)

def encrypt_oracle(user_bytes: bytes) -> bytes:
    plaintext = user_bytes + FLAG
    padded = pad(plaintext, BLOCK_SIZE)
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(padded)

print("=== AES-ECB Byte-at-a-Time Oracle ===")
print("Send hex-encoded bytes. Empty line or 'exit' quits.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Listening on {HOST}:{PORT}...")
    conn, addr = server_socket.accept()
    
    with conn:
        print(f"Connected by {addr}")

        while True:
            conn.sendall("> ".encode())
            data = conn.recv(1024)
            if not data:
                break

            line = data.strip()
            print("line: ", line)
            if not line or line.lower() == 'exit':
                print("Bye!")
                break

            try:
                user_bytes = binascii.unhexlify(line)
            except (binascii.Error, ValueError):
                print("[!] That doesn't seem like a proper spell.")
                continue

            ct = encrypt_oracle(user_bytes)
            print("binascii.hexify(ct) decode: ", binascii.hexlify(ct).decode())            
            conn.sendall(binascii.hexlify(ct))
