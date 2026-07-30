class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        

        for i in range(32):
            bit = n & 1
            n = n >> 1

            rev = rev << 1
            rev = rev | bit
            

        return rev
            
