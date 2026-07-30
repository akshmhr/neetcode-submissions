class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Xor = n
        for i in range(n):
            Xor = Xor ^ i
            Xor = Xor ^ nums[i]


        return Xor