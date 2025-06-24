# This script reads the content of 'bytes.txt', skips the header line,
# and applies the inverse transformation to recover the original bytes.
# It then writes these recovered bytes to a new file named 'hello_recovered.c'.

def recover_original_bytes(transformed_data_string, key):
    """
    Reverses the 'not_so_fast' transformation. It subtracts the key
    from each character's ordinal value and wraps the result around 256.

    Args:
        transformed_data_string: The string containing the transformed (encrypted) data.
        key: The integer key used for the original transformation.

    Returns:
        A bytes object representing the recovered original data.
    """
    recovered_bytes_list = []
    for char_code in transformed_data_string:
        # Convert the character back to its integer (ordinal) value.
        # Subtract the key and apply modulo 256 to ensure the result is
        # within the 0-255 range, correctly handling negative results.
        original_byte_value = (ord(char_code) - key) % 256
        recovered_bytes_list.append(original_byte_value)

    # Convert the list of integer byte values into a bytes object.
    return bytes(recovered_bytes_list)

##########
DECRYPTION_KEY = 9

input_filename = "01_bytes.txt"
output_filename = "02_elf.txt"

try:
    with open(input_filename, "r", encoding='latin-1') as file:
        lines = file.readlines()

        # The first line is the header, so skip it.
        # Concatenate the remaining lines to get the transformed data.
        # Use .join() with "" to ensure no extra newlines are introduced
        # if there were any within the transformed data itself.
        if len(lines) > 0:
            header_line = lines[0] # Store the header line
            transformed_data_string = "".join(lines[1:])
        else:
            print(f"Error: '{input_filename}' is empty or only contains the header.")
            exit()

    print(header_line)
    print(f"Successfully read '{input_filename}'.")

except FileNotFoundError:
    print(f"Error: '{input_filename}' not found. Please make sure it's in the same directory.")
    exit()
except Exception as e:
    print(f"An error occurred while reading '{input_filename}': {e}")
    exit()

print("Recovering original bytes...")
recovered_data = recover_original_bytes(transformed_data_string, DECRYPTION_KEY)

# --- Write the recovered data to hello_recovered.c ---
try:
    # Open the output file in binary write mode ('wb')
    # This is important because the recovered data is a bytes object,
    # and we want to write it as raw bytes, not as a text string that
    # might get re-encoded.
    with open(output_filename, "wb") as file:
        file.write(recovered_data)
    print(f"Recovered data written to '{output_filename}' successfully.")
    print(f"You can now inspect '{output_filename}' to verify the content.")

except Exception as e:
    print(f"An error occurred while writing to '{output_filename}': {e}")

