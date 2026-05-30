class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        mL = 0
        for i in range(len(height)):
            mL = max(height[i], mL)
            max_left[i] = mL
        
        j = len(height) - 1
        mR = 0
        for j in range(len(height)-1, -1, -1):
            mR = max(mR, height[j])
            max_right[j] = mR

        res = 0
        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]

        return res

        
        
        
        

            
