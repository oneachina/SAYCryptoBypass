from Crypto.Util.strxor import strxor
import re

def encrypt(plaintext, key="SAY"):
    shift_bits = sum(ord(c) for c in key) % 7 + 1
    xor_keys = key.encode()
    block_size = max(1, len(key))
    
    shifted = bytes((b >> shift_bits) | ((b << (8 - shift_bits)) & 0xFF) 
                  for b in plaintext.encode())
    
    xored = bytes(b ^ xor_keys[i % len(xor_keys)] for i, b in enumerate(shifted))
    
    padding = block_size - (len(xored) % block_size
    padded = xored + bytes([padding] * padding)
    blocks = [padded[i:i+block_size] for i in range(0, len(padded), block_size)]
    reversed_blocks = b"".join(block[::-1] for block in blocks)
    
    return reversed_blocks.hex().upper()

device_id = input("Device id: ")
activation_code = encrypt(device_id)
print(f"Activation code: {activation_code}")
