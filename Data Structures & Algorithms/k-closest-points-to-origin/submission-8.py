import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = -((point[0]**2) + (point[1]**2))
            if len(heap)<k:
                heapq.heappush(heap, (distance, point))
            else:
                if distance > heap[0][0]:
                    heapq.heapreplace(heap, (distance, point))
        
                
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
            
