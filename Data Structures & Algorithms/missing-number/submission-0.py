class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Sum = sum(nums)
        n = len(nums)
        missing = ( (n*(n+1))//2 ) - Sum

        return missing