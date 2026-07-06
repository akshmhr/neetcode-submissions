class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        n1 = len(s)
        n2 = len(t)
        if n1 != n2 :
            return False
        
        for i in range(n1):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            hash_map[t[i]] = hash_map.get(t[i], 0) - 1

        for i in hash_map:
            if hash_map[i] != 0:
                return False
        return True
