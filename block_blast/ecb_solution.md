### Simple netcat example

SERVER

```
─$ nc -l -p 12345 -s 127.0.0.1 | python3 eg_server.py
Server started. Waiting for input...
Received: Hello, server! This is the client.
```

CLIENT

```
$ python3 client_eg.py

$ cat client_eg.py 
import socket

HOST = "127.0.0.1"
PORT = 12345
MESSAGE = "Hello, server! This is the client.\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(MESSAGE.encode())
```

### challenge.py with prompt ">"

The simple example must be enhanced so the server sends a prompt and the client strips the prompt 

