class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right-left
            area = width * min(heights[left], heights[right])
            Max = max(area, Max)

            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1

        return Max