class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # go one from the left and one from the right
        # have a left max and a right max
        # when the pointers meet each other, stop
        # calculate the area and return it
        # O(n) runtime
        # O(2) space
        
        # [1,7,2,5,4,7,3,6]
        # left = 1
        # right = 5
        # maxArea = 36

        left, right = 0, len(heights) - 1
        maxArea = 0

        # Get the maximums
        while left < right:
            currentArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, currentArea)
            if heights[left] <= heights[right]:
                left+=1  
            else:
                right-=1
        
        return maxArea