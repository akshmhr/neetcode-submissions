class Solution:
    def canFinish(self, piles, h, speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            if self.canFinish(piles, h, mid):
                right = mid
            else:
                left = mid+1


        return right
    



