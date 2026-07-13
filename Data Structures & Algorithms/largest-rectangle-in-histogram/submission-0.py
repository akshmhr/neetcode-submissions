class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n = len(heights)

        for i in range(n+1):
            if i == n:
                currentHeight = 0
            else:
                currentHeight = heights[i]
            
            while (stack) and currentHeight < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                maxArea = max(maxArea, height*width)

            
            stack.append(i)

        
        return maxArea


