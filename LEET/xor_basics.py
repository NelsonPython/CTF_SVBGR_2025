'''
EXPECTED RESULTS:

KE  00000010
s1  00000101
s2  00000011

s1 ^ key:  00000111
key ^ s1:  00000111
s2 ^ key:  00000001
key ^ s2:  00000001
'''

key = 2
key_bytes = key.to_bytes(1, byteorder='big')
bit_key = bin(int.from_bytes(key_bytes, byteorder='big'))[2:].zfill(8) 
print("KE ", bit_key)

s1 = 5
s1_bytes = s1.to_bytes(1, byteorder='big')
bit_representation_1 = bin(int.from_bytes(s1_bytes, byteorder='big'))[2:].zfill(8) 
print("s1 ", bit_representation_1)

s2 = 3
s2_bytes = s2.to_bytes(1, byteorder='big')
bit_representation_2 = bin(int.from_bytes(s2_bytes, byteorder='big'))[2:].zfill(8) 
print("s2 ",bit_representation_2)

print("")

def showBits(xor_bytes):
    return bin(int.from_bytes(xor_bytes, byteorder='big'))[2:].zfill(8)

# XOR operations
xor_result = s1 ^ key
xor_bytes = xor_result.to_bytes(1, byteorder='big')
print("s1 ^ key: ", showBits(xor_bytes))

xor_result = key ^ s1
xor_bytes = xor_result.to_bytes(1, byteorder='big')
print("key ^ s1: ", showBits(xor_bytes))

xor_result = s2 ^ key
xor_bytes = xor_result.to_bytes(1, byteorder='big')
print("s2 ^ key: ", showBits(xor_bytes))

xor_result = key ^ s2
xor_bytes = xor_result.to_bytes(1, byteorder='big')
print("key ^ s2: ", showBits(xor_bytes))


