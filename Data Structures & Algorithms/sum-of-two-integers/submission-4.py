class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        MAX = 0x7fffffff

        while b:
            temp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = temp

        return a if a <= MAX else ~(a ^ mask)