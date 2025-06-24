def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

# Secret key (UNKNOWN to attacker)
hidden_key = "SECRET"
original_text = "THIS IS OUR CLASSIFIED HELLO WORLD"

ciphertext = xor_encrypt_decrypt(original_text, hidden_key)
print("Ciphertext:", ciphertext.encode('utf-8'))

# recover secret key using the actual known phrase
known_word = original_text
# recover the secret key using a partially known phrase
known_word = "THIS IS OUR CLASSIFIED HELLO WORLD"
key_guess = ''.join(chr(ord(ciphertext[i]) ^ ord(known_word[i])) for i in range(len(known_word)))
print("Recovered key guess:", key_guess)
print("\n")

cipherbytes = ciphertext.encode('utf-8')

words = ["WORLD", "HELLO", "IS", "THIS", "LEET", "SECRET"]

for word in words:
    word_bytes = word.encode()
    for i in range(len(cipherbytes) - len(word_bytes) + 1):
        potential_key = bytes([cipherbytes[i + j] ^ word_bytes[j] for j in range(len(word_bytes))])
        print(f"Potential Key at position {i} for {word}: {potential_key.decode(errors='ignore')}")
    print('\n')
