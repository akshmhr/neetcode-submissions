class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        occurance = [0]*26
        left = ans = max_occurance = 0

        for right in range(n):
            index = ord(s[right]) - ord('A')
            occurance[index] += 1
            max_occurance = max(max_occurance, occurance[index])


            if (right - left + 1 - max_occurance > k):
                occurance[ord(s[left]) - ord('A')] -= 1
                left +=1

            
            ans = max(ans, right-left+1)

        return ans