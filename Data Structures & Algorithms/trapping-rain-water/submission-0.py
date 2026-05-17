class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [-1] * n
        right = [-1] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        result = 0
        for j in range(n):
            result += (min(left[j], right[j]) - height[j])
        
        return result