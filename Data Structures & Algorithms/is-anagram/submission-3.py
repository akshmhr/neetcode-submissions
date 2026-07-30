class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countChar = [0] * 26

        for i in s:
            countChar[ord(i) - ord('a')]+=1

        for j in t:
            countChar[ord(j) - ord('a')]-=1

        if countChar == [0]*26:
            return True
        
        return False

