class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)==0 or len(t) == 0 or len(s) < len(t):
            return ""


        mapT = {}
        for i in range(len(t)):
            mapT[t[i]] = mapT.get(t[i], 0) + 1


        required = len(mapT)
        l = r = 0
        create = 0 
        ans = [-1, 0, 0]

        subStringMap = {}

        while r < len(s):
            c = s[r]
            count = subStringMap.get(c, 0)
            subStringMap[c] = count+1

            if c in mapT and mapT[c] == subStringMap[c]:
                create+=1
            
            while (l <= r) and create == required:
                c = s[l]
                if ans[0] == -1 or ans[0] >= r-l+1:
                    ans[0] = r-l+1
                    ans[1] = l
                    ans[2] = r
                
                subStringMap[c] -= 1
            
                if c in mapT and subStringMap[c] < mapT[c]:
                    create -= 1
                
                l+=1
            
            r+=1

        if ans[0] == -1:
            return ""
        return s[ans[1]: ans[2]+1]


