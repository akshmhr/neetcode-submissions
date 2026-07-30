import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        

        while len(heap) > 1:
            a = -(heapq.heappop(heap))
            if heap:
                b = -(heapq.heappop(heap))
                temp = abs(a-b)

                if temp!=0:
                    heapq.heappush(heap, -temp)
                elif (not heap):
                    return 0
        
        return abs(heap[0])

