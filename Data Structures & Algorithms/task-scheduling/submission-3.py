class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        l = len(tasks)
        Max = 1
        for i in tasks:
            hashMap[i] = hashMap.get(i, 0) + 1
            Max = max(hashMap[i], Max)

        maxCount = 0
        for freq in hashMap.values():
            if freq == Max:
                maxCount += 1

        formula = ((Max-1)*(n+1)) + maxCount
        return max(l, formula)
        
