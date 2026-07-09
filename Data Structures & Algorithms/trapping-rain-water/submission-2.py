class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [-1] * n
        right = [-1] * n 

        for i in range(n):
            if i ==0:
                left[i] = height[i]
                continue
            
            if height[i] > left[i-1]:
                left[i] = height[i]
            
            else:
                left[i] = left[i-1]


        for i in range(n-1, -1, -1):
            if i==n-1:
                right[i] = height[i]
                continue
            
            if height[i] > right[i+1]:
                right[i] = height[i]
            
            else:
                right[i] = right[i+1]

        # print(left)
        # print(right)
        # print(height)
        water = 0
        for i in range(n):
            water += (min(left[i], right[i])) - height[i]

        return water
