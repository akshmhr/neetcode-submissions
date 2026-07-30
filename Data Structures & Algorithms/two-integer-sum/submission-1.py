class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)

        for i in range(n):
            find = target-nums[i]

            if find in hash_map:
                return [hash_map[find], i]
            
            hash_map[nums[i]] = i


