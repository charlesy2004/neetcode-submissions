class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        alist = [1] * len(nums)
        for i in range(len(nums)):
            j = 0
            while j < len(nums):
                if j != i:
                    alist[i] *= nums[j]
                j += 1
        return alist
        