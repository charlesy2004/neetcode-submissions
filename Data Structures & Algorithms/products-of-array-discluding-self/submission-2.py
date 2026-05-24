class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        alist = [1] * len(nums)
        for i in range(1, len(nums)):
            alist[i] = alist[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            alist[i] = alist[i] * suffix
        # for i in range(len(nums)):
        #     alist[i] = prefix[i] * suffix[i]
        return alist