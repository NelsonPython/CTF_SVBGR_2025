'''
    5c623c61545f63270c4047724e114d52794e16485f7b4e034433652b1744527b2b0520
    40612c0653687b270649477e20065e4667311549566823044f4c7e201e435f762d0a7c

    PLAN, NEVER, SECRET, OUR, HIGHER, CLASSIFIED, WILL, and BE

    offset 0: P1='OUR ULTIMATE PLAN WILL BE REVEALED' -> Potential P2='SVBGR{LIGHTING_UP_THE_MEN_IN_BLACK' 
'''
import itertools
import base64

c1_hex = "5c623c61545f63270c4047724e114d52794e16485f7b4e034433652b1744527b2b0520"
c2_hex = "40612c0653687b270649477e20065e4667311549566823044f4c7e201e435f762d0a7c"
cipherbytes_1 = bytes.fromhex(c1_hex)
cipherbytes_2 = bytes.fromhex(c2_hex)

p1_xor_p2_result = bytearray()

if len(cipherbytes_1) != len(cipherbytes_2):
    print("Error: The ciphertexts have different lengths. Cannot perform direct XOR.")
else:
    # Iterate through the bytes of both ciphertexts
    # and perform a bitwise XOR operation on corresponding bytes.
    for i in range(len(cipherbytes_1)):
        # XOR the i-th byte of cipherbytes_1 with the i-th byte of cipherbytes_2
        # and append the result to our bytearray.
        p1_xor_p2_result.append(cipherbytes_1[i] ^ cipherbytes_2[i])
    
    print("--- Result of C1 XOR C2 (which equals P1 XOR P2) ---")
    
    # Print the result in hexadecimal format for easy inspection
    print("Hexadecimal (P1 XOR P2):")
    print(p1_xor_p2_result.hex())
    
    # Attempt to decode the result as ASCII.
    # This might produce mostly gibberish if the plaintexts are very different,
    # but it can sometimes reveal readable segments if parts of P1 and P2
    # are similar or if certain plaintext patterns exist (e.g., spaces).
    print("\nAttempting to decode as ASCII (errors ignored for unprintable characters):")
    print(p1_xor_p2_result.decode(errors='ignore'))

    print("\n--- End of P1 XOR P2 Analysis ---")

# I did not automate checking each of these words.  I did this manually until
# I found the plaintext for p1:  OUT ULTIMATE PLAN WILL BE REVEALED
words = ["PLAN", "NEVER", "SECRET", "OUR", "HIGHER", "CLASSIFIED", "WILL", "BE", "LEET"]

# Our crib: A word we suspect might be in Plaintext 1 (P1)
p1_xor_p2_bytes = p1_xor_p2_result

crib_p1_str = "OUR ULTIMATE PLAN WILL BE REVEALED"
crib_p1_bytes = crib_p1_str.encode('ascii')

print(f"Attempting to crib-drag with: '{crib_p1_str}'")
print("-" * 50)

# Iterate through every possible starting offset where the crib could fit
max_offset = len(p1_xor_p2_bytes) - len(crib_p1_bytes)

if max_offset < 0:
    print(f"Crib '{crib_p1_str}' is too long to fit in the P1 XOR P2 result.")
else:
    for offset in range(max_offset + 1):
        # Extract the segment from P1 XOR P2 that corresponds to the current offset.
        p1_xor_p2_segment = p1_xor_p2_bytes[offset : offset + len(crib_p1_bytes)]

        # Perform the crib-dragging XOR: Crib_P1 XOR (P1 XOR P2)_segment = P2_revealed_segment
        potential_p2_segment = bytearray()
        for i in range(len(crib_p1_bytes)):
            potential_p2_segment.append(crib_p1_bytes[i] ^ p1_xor_p2_segment[i])

        # Attempt to decode the revealed segment as ASCII.
        decoded_p2_segment = potential_p2_segment.decode('ascii', errors='ignore')
        print(f"Offset {offset}: P1='{crib_p1_str}' -> Potential P2='{decoded_p2_segment}' (Hex: {potential_p2_segment.hex()})")

print("-" * 50)
print("--- Crib-Dragging Complete ---")

#Offset 0: P1='OUR' -> Potential P2='SVB' (Hex: 535642)

