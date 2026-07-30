class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        l = len(tasks)
        maxFreq = 1
        for i in tasks:
            hashMap[i] = hashMap.get(i, 0) + 1
            maxFreq = max(hashMap[i], maxFreq)

        maxCount = 0
        for freq in hashMap.values():
            if freq == maxFreq:
                maxCount += 1

        formula = ((maxFreq-1)*(n+1)) + maxCount
        return max(l, formula)
        
