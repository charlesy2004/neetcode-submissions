class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            contained = (r - l) * min(heights[l], heights[r])
            if contained > max_res:
                max_res = contained
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_res