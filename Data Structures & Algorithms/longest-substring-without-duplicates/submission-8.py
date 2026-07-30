class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        hash_set = set()
        count = 0

        for right in range(n):
    
            while s[right] in hash_set and (left<right):
                hash_set.remove(s[left])
                left+=1
                
                        
            hash_set.add(s[right])
            count = max(count, right-left+1)
        return count


