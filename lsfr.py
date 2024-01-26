class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps

    def step(self):
        xor = 0
        for t in self.taps:
            xor ^= (self.state >> t) & 1
        self.state = (self.state >> 1) | (xor << 7)
        return xor
