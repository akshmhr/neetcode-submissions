class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            local_target = target - nums[i]
            if local_target in hash_map:
                return [hash_map[local_target], i]
            hash_map[nums[i]] = i
