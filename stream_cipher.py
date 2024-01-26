def generate_keystream(lfsr, length):
    return [lfsr.step() for _ in range(length)]

def xor_with_keystream(data, keystream):
    return bytes([b ^ (k << 7) for b, k in zip(data, keystream)])
