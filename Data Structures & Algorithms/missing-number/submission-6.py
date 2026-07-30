class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Xor = n
        for i in range(n):
            Xor ^= i ^ nums[i]
        
        return Xor