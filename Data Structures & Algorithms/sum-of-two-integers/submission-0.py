class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # simulate 32-bit integer overflow

        while b != 0:
            # sum without carry
            bit_sum = (a ^ b) & MASK
            # carry
            carry = ((a & b) << 1) & MASK

            a, b = bit_sum, carry

        # handle negative numbers
        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ MASK)
