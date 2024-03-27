# - LFSR Stream Cipher

## Overview

This project involves a known plaintext attack on a stream cipher that employs a Linear Feedback Shift Register (LFSR) as a pseudo-random bit generator. You are provided with a ciphertext (`proj1_ciphertext.bin`) encrypted using the stream cipher and the initial segment of the plaintext (`proj1_known-plaintext.txt`). The goal is to decrypt the remaining portion of the ciphertext.

## Instructions

1. **Files Provided:**
   - `proj1_ciphertext.bin`: The encrypted ciphertext.
   - `proj1_known-plaintext.txt`: The first part of the plaintext.

2. **Objective:**
   - Decrypt the remaining portion of the ciphertext using the provided LFSR-based stream cipher.

3. **Implementation Details:**
   - The encryption process uses the classes and functions introduced during the lessons.
   - Pay attention to the little/big-endian representation of bytes.

## Project Structure

### Files
- `main.py`: The main script that initializes the LFSR, generates a keystream, encrypts the plaintext, and attempts to decrypt the ciphertext.
- `lsfr.py`: Module containing the LFSR class, representing the Linear Feedback Shift Register.
- `stream_cipher.py`: Module with functions for generating a keystream and XORing data with the keystream.

### Running the Project
1. Ensure that the required modules (`lsfr` and `stream_cipher`) are available in your Python environment.
2. Run the `main.py` script to initiate the decryption process.

### Notes
- Be mindful of the little/big-endian representation of bytes when processing the ciphertext.
- The ciphertext has been generated using the provided classes and functions discussed in the lessons.

Feel free to explore the code and experiment with different approaches to decrypt the remaining ciphertext. If you encounter any issues or have questions, please refer to the provided documentation or seek assistance. Good luck with your decryption efforts!
