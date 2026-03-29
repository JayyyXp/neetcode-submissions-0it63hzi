class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit_i = ((n >> i) & 1)
            if bit_i:
                res |= (1 << (31 - i))

        return res