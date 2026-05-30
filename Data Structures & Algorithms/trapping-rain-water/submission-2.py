class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left = [0] * len(height)
        # max_right = [0] * len(height)
        # mL = 0
        # for i in range(len(height)):
        #     mL = max(height[i], mL)
        #     max_left[i] = mL
        
        # j = len(height) - 1
        # mR = 0
        # for j in range(len(height)-1, -1, -1):
        #     mR = max(mR, height[j])
        #     max_right[j] = mR

        # res = 0
        # for i in range(len(height)):
        #     res += min(max_left[i], max_right[i]) - height[i]

        # return res
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        i = 0
        res = 0
        while l < r:
            
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if maxL <= maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1   
        return res

        
        
        
        

            
