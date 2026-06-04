class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for num in nums:
        #     minim = min(num, minim)
        # return minim
        l = 0
        r = len(nums) - 1
        
        while l < r:
            curr = (l + r)// 2
            if nums[curr] > nums[r]:
                l = curr + 1
            else:
                r = curr
        return nums[l]

        
