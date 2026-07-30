import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        

        while len(heap) > 1:
            a = -(heapq.heappop(heap))
        
            b = -(heapq.heappop(heap))
            

            if a!=b:
                heapq.heappush(heap, b-a)
        
        
        if heap:
            return abs(heap[0])

        return 0

