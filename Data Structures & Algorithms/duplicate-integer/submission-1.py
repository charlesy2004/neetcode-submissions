class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alist = []
        for i in range(len(nums)):
            alist = [num for index, num in enumerate(nums) if index != i]
            if nums[i] in alist:
                return True
        return False