from lsfr import LFSR
from stream_cipher import generate_keystream, xor_with_keystream
import os

def main():
    # Initialize LFSR with the chosen seed and taps
    seed = int('10101010', 2)
    taps = [7, 5, 3, 1]
    lfsr = LFSR(seed, taps)

    # The plaintext "HELLO"
    plaintext = "HELLO HOW ARE YOU".encode()

    # Generate a keystream of the same length as the plaintext
    keystream_length = len(plaintext) * 8  # 8 bits per character
    keystream = generate_keystream(lfsr, keystream_length)

    # Encrypt the plaintext
    ciphertext = xor_with_keystream(plaintext, keystream)

        # Save ciphertext and known plaintext to files
    with open("proj1_ciphertext.bin", "wb") as f:
        f.write(ciphertext)

    with open("proj1_known-plaintext.txt", "wb") as f:
        f.write(plaintext[:2])  # Use the first two bytes as the known part
    
        # Load the ciphertext and known plaintext
    ciphertext_filename = "proj1_ciphertext.bin"
    known_plaintext_filename = "proj1_known-plaintext.txt"

    if not (os.path.exists(ciphertext_filename) and os.path.exists(known_plaintext_filename)):
        print("Error: Input files not found.")
        return

    with open(ciphertext_filename, "rb") as f:
        ciphertext = bytearray(f.read())

    with open(known_plaintext_filename, "rb") as f:
        known_plaintext = bytearray(f.read())
        
    # Decrypt the ciphertext (using the same keystream)
    decrypted_text = xor_with_keystream(ciphertext, keystream)

    print("Length of Ciphertext:", len(ciphertext))
    print("Length of Known Plaintext:", len(known_plaintext))
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)

if __name__ == '__main__':
    main()
