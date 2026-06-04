class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # return nums[l]
        if target > nums[-1]:
            l_l = 0
            l_r = l
        else:
            l_l = r
            l_r = len(nums) - 1
        while l_l <= l_r:
            m = (l_l + l_r)//2
            if target > nums[m]:
                l_l = m + 1
            elif target < nums[m]:
                l_r = m - 1
            else:
                return m
        return -1


        