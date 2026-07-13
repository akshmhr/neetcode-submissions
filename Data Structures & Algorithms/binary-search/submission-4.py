class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            midIndex = (l+r) //2

            if nums[midIndex] == target:
                return midIndex

            if nums[midIndex] < target:
                l = midIndex + 1
                continue
            elif nums[midIndex] > target:
                r = midIndex - 1
                continue
        return -1