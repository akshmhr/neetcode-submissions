class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Xor = 0
        for i in range(n):
            Xor = Xor ^ i
            Xor = Xor ^ nums[i]


        return Xor^n