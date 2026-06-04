class Solution:
    def findMin(self, nums: List[int]) -> int:
        minim = float("inf")
        # for num in nums:
        #     minim = min(num, minim)
        # return minim
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            curr = (l + r)// 2
            if nums[curr] > nums[r]:
                l = curr + 1
            elif nums[curr] < nums[r]:
                r = curr
            elif nums[curr] == nums[r] or nums[curr] == nums[l]:
                return nums[curr]

        
