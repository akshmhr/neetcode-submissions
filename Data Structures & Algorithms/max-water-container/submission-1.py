class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        current, maxx = 0, 0
        l, r = 0, n - 1

        while l < r:
            current = min(height[l], height[r]) * (r - l)
            maxx = max(maxx, current)
            while (l < r) and height[l] <= height[r]:
                l += 1
                current = min(height[l], height[r]) * (r - l)
                maxx = max(maxx, current)
            while (l < r) and height[l] > height[r]:
                r -= 1
                current = min(height[l], height[r]) * (r - l)
                maxx = max(maxx, current)
        return maxx
