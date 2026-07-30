import heapq

class MedianFinder:

    def __init__(self):
        self.small = []      # max heap
        self.large = []      # min heap

    def addNum(self, num):

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        if self.small and self.large and (-self.small[0] > self.large[0]):
            a = -heapq.heappop(self.small)
            b = heapq.heappop(self.large)

            heapq.heappush(self.small, -b)
            heapq.heappush(self.large, a)

    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2