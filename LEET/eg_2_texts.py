def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

# Secret key (UNKNOWN to attacker)
hidden_key = "SECRET"
original_text_1 = "THIS IS OUR CLASSIFIED HELLO WORLD"
original_text_2 = "CLASSIFIED BIRDS SAY HELLO WORLD"

ciphertext_1 = xor_encrypt_decrypt(original_text_1, hidden_key)
print("ciphertext_1:", ciphertext_1.encode('utf-8'))
ciphertext_2 = xor_encrypt_decrypt(original_text_2, hidden_key)
print("")
print("ciphertext_2:", ciphertext_2.encode('utf-8'))

# recover secret key using the actual known phrase
known_word = original_text_1
key_guess = ''.join(chr(ord(ciphertext_1[i]) ^ ord(known_word[i])) for i in range(len(known_word)))
print("")
print("Using known text, recovered key guess 1:", key_guess)

# recover secret key using the actual known phrase
known_word = original_text_2
key_guess = ''.join(chr(ord(ciphertext_2[i]) ^ ord(known_word[i])) for i in range(len(known_word)))
print("Using known text, recovered key guess 2:", key_guess)
print("\n")

cipherbytes_1 = ciphertext_1.encode('utf-8')
cipherbytes_2 = ciphertext_2.encode('utf-8')

words = ["WORLD", "HELLO", "IS", "THIS", "LEET", "SECRET"]

for word in words:
    word_bytes = word.encode()

    i = 0
    while i <= len(cipherbytes_1) - len(word_bytes):
        potential_key_1 = bytearray()
        potential_key_2 = bytearray()
        
        j = 0
        while j < len(word_bytes):
            try:
                potential_key_1.append(cipherbytes_1[i + j] ^ word_bytes[j])
            except:
                pass
            try:
                potential_key_2.append(cipherbytes_2[i + j] ^ word_bytes[j])
            except:
                pass

            j += 1

        print("Potential Key at position", i, "for", word, ":", potential_key_1.decode(errors='ignore'))
        print("Potential Key at position", i, "for", word, ":", potential_key_2.decode(errors='ignore'))
        print("")
        i += 1

    print("\n")
