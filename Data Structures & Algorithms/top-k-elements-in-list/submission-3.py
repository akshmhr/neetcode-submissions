class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq.items():
            bucket[freq].append(num)

    
        ans = []

        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                ans.append(j)

                if len(ans) == k:
                    return ans