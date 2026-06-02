class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        minL = float("inf")
        minR = float("inf")
        left_min = []
        
        for i in range(len(heights)):
            ind = i
            while stack and heights[i] < stack[-1][0]:
                val, ind = stack.pop()
                curr_area = val * (i - ind)
                if curr_area > max_area:
                    max_area = curr_area
            stack.append((heights[i], ind))
        while stack:
            val, ind = stack.pop()
            curr_area = val * (len(heights) - ind)
            if curr_area > max_area:
                max_area = curr_area
        # max_area = max(len(heights) * left_min[-1], curr_area)
        return max_area
        
            
            

        