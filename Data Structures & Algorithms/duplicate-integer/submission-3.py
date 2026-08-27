class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set(nums)
        if len(hash_set) != len(nums):
            return True
        
        return False
            
