### Classic xor
XOR encryption is simple but not secure when parts of the plaintext are known or can be easily guessed.

### xor Basics
[xor_basics.py](xor_basics.py) contains a simple example of xor operations:

```
$ python3 xor_basics.py

KEY  00000010
s1   00000101
s2   00000011

s1 ^ key:  00000111
key ^ s1:  00000111
s2 ^ key:  00000001
key ^ s2:  00000001
```

### Example 1:

The xor_encrypt_decrypt(text, key) function in [eg_1_text.py](eg_1_text.py) encrypts or decrypts the input text by applying the XOR (^) operation between each character of the text and the corresponding character of the key.  If the text is longer than the key, then the key repeats.  In this example, a secret key called ``` hidden_key = "SECRET" ``` is used to encrypt the text ``` THIS IS OUR CLASSIFIED HELLO WORLD ``` and produce a ciphertext: 
```
b'\x07\r\n\x01e\x1d\x00e\x0c\x07\x17t\x10\t\x02\x01\x16\x1d\x15\x0c\x06\x16e\x1c\x16\t\x0f\x1de\x03\x1c\x17\x0f\x16'
```

If an attacker knows part or all of the original text, they can recover parts of the key by using the XOR operation.  This script demonstrates key recovery by XOR-ing the ciphertext with each known word from a list of words ``` ["WORLD", "HELLO", "IS", "THIS", "LEET", "SECRET"] ``` including words from the plain text.

```
key_guess = ''.join(chr(ord(ciphertext[i]) ^ ord(known_word[i])) for i in range(len(known_word)))
```
The recovered key guess is SECRETSECRETSECRETSECRETSECRETSECR.  Given that the key repeats, the key is "SECRET"

```
$ python3 eg_1_text.py
```


### Example 2:

[eg_2_texts.py](eg_2_texts.py) has two different plaintexts and features old-fashioned coding loops

```
$ python3 eg_2_texts.py
```


### Decoding with crib dragging

[xor_leet_w_crib_dragging.py](xor_leet_w_crib_dragging.py) is the code that found the flag.  It contains documentation.

```
$ python3  xor_leet_w_crib_dragging.py
```

