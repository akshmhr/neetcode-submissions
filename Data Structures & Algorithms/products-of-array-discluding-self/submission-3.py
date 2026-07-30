class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix = [1] * n


        product = 1
        for i in range(n):
            left_prefix[i] = product
            product*=nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            left_prefix[i] *= product
            product*=nums[i]


        return left_prefix


