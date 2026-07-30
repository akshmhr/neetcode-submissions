import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(heap, (distance, point))

        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
            
