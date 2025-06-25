### Simple netcat example

Setup a test environment on your local machine running the server in one window and the client in another:

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

### AES-ECB Vulnerability

Launch a "byte-at-a-time" attack against an AES-ECB (Electronic Codebook) encryption oracle. The goal of such an attack is to decrypt an unknown secret string that is being appended to user-controlled input before encryption.  First, get the block size because ECB is encrypted by block.  Get the length of the block by inputting progressively longer strings until the size of the output changes.  You can test this manually by entering progressivly longer input strings.

```
└─$ python3 challenge.py     
=== AES-ECB Byte-at-a-Time Oracle ===
Send hex-encoded bytes. Empty line or 'exit' quits.
> AA
fc34001d67988205740a7aa74763abd3
> AAAA
3ff55be1da29b0435b8d5a166a880a68
> AAAAAA
c730f12d118813e9519a027f9124bc92
> AAAAAAAA
1d5d50a8938f2e9051437268eb9cf3b1
> AAAAAAAAAA
ba27d73127e910b67c62528923de9c19e249d64baf9bc0d00448d3a9d0e6e14f
> AAAAAAAAAAAA
585cb0ff0f22b11574df564e8fac1a484ed9614e5775e57953d71fd8368e7acd
> AAAAAAAAAAAAAA
b11bdbe057fb456f2c77285d8b41a50454452924c581aab20e3405e1444ca7bd
> AAAAAAAAAAAAAAAA
b26fb8ccdd3471624e25963fca2bdba00bb9cbfe7c788041c3ff9dfdd9972e7a
> AAAAAAAAAAAAAAAA
b26fb8ccdd3471624e25963fca2bdba00bb9cbfe7c788041c3ff9dfdd9972e7a
```

During the competition, I wrote a script that launched the attack, but it timed out.  I also ran out of time to troubleshoot.  After the competition, I reviewed solve.py and learned that I should have used a ``` while ``` loop to avoid this.  

Inside the ``` while ``` loop, the number of bytes needed to fill the current block are computed leaving room for a guess about the next byte.  An oracle function sends user-provided bytes to the server and receives ciphertext from the server.  See the [solution writeup](https://github.com/jselliott/USCyberOpen2025/tree/main/challenges/bgr/block-blast-crypto)    


I was able to solve this after the competition by running solve.py in my test environment.

```
$ python3 02_solve_flag.py  
[*]  Starting byte-at-a-time attack
[+]  Recovered byte 01: b'S'
[+]  Recovered byte 02: b'V'
[+]  Recovered byte 03: b'B'
[+]  Recovered byte 04: b'G'
[+]  Recovered byte 05: b'R'
[+]  Recovered byte 06: b'{'
[+]  Recovered byte 07: b'f'
[+]  Recovered byte 08: b'l'
[+]  Recovered byte 09: b'a'
[+]  Recovered byte 10: b'g'
[+]  Recovered byte 11: b'}'

FLAG: SVBGR{flag}
```

