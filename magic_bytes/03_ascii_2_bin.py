import binascii

filename = "02_elf.txt"
with open(filename,"r") as f:
    CHALLENGE_HEX_STRING = f.read()

# The standard ELF magic number (first 4 bytes)
# 0x7F 'E' 'L' 'F' in byte format
ELF_MAGIC = b'\x7fELF'

def decrypt_bytes(encrypted_bytes_obj, key):
    """
    Applies the inverse Caesar cipher-like shift to each byte,
    ensuring the result stays within the byte range (0-255) using modulo 256.

    Args:
        encrypted_bytes_obj: A bytes object containing the encrypted data.
        key: The integer key to subtract from each byte.

    Returns:
        A new bytes object with each byte shifted back by the key.
    """
    decrypted_byte_list = []
    for b in encrypted_bytes_obj:
        # Subtract the key and apply modulo 256 to ensure the result is
        # within the 0-255 range, correctly handling potential negative values.
        decrypted_value = (b - key) % 256
        decrypted_byte_list.append(decrypted_value)
    return bytes(decrypted_byte_list)

# --- Main decryption logic ---
print("Attempting to decrypt the CTF challenge ELF...")

try:
    # Convert the hexadecimal string to a bytes object
    # We use .upper() to ensure it's always uppercase, which binascii.unhexlify prefers
    encrypted_elf_bytes = binascii.unhexlify(CHALLENGE_HEX_STRING.upper())
except binascii.Error as e:
    print(f"Error converting hex string to bytes: {e}")
    print("Please ensure the hexadecimal string is valid (even number of characters, only hex digits).")
    exit()

found_key = None
recovered_elf_content = None

# Brute-force the key from 1 to 255
for key_attempt in range(256): # range(256) covers 0-255
    # Decrypt only the first 4 bytes to check for the magic number
    candidate_magic = decrypt_bytes(encrypted_elf_bytes[:4], key_attempt)

    if candidate_magic == ELF_MAGIC:
        found_key = key_attempt
        print(f"\nPotential key found: {found_key}")
        print(f"Decrypted magic: {candidate_magic.hex().upper()} (matches {ELF_MAGIC.hex().upper()})")

        # If magic matches, decrypt the entire ELF content
        recovered_elf_content = decrypt_bytes(encrypted_elf_bytes, found_key)
        break # Stop searching, we found the key!

if found_key is not None:
    output_filename = "ctf_challenge_recovered_elf"
    try:
        # Write the recovered bytes to a new binary file
        with open(output_filename, "wb") as f:
            f.write(recovered_elf_content)
        print(f"Full ELF recovered and saved to '{output_filename}'")
        print("\n--- Next Steps ---")
        print(f"1. Make the recovered file executable:")
        print(f"   chmod +x {output_filename}")
        print(f"2. Run the executable to find the flag:")
        print(f"   ./{output_filename}")
    except Exception as e:
        print(f"An error occurred while writing the recovered ELF: {e}")
else:
    print("No valid key found that decrypts the first 4 bytes to ELF magic.")
    print("This might mean the encryption method is different, or the hex string is corrupted.")

