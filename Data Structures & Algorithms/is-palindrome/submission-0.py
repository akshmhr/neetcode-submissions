class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1
        s = s.lower()
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1

            while start < end and not s[end].isalnum():
                end -= 1
            if s[start] != s[end]:
                return False
            start +=1
            end -= 1
        return True