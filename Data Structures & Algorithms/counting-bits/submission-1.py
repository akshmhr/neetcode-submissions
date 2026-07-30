class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            if i==0:
                ans.append(0)            
            else:
                temp = i
                count = 0
                while temp != 0:
                    temp = temp & (temp-1)
                    count+=1
                
                ans.append(count)

        
        return ans
