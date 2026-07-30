class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix = [1] * n
        right_prefix = [1] * n


        i = 0
        product = 1
        for i in range(n):
            left_prefix[i] = product
            product*=nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            right_prefix[i] = product
            product*=nums[i]

        ans = []

        for i in range(n):
            ans.append(left_prefix[i] * right_prefix[i])


        return ans


