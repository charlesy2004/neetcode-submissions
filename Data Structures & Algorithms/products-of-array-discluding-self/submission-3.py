class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            j = 0
            product = 1
            while j < len(nums):
                if j != i:
                    product *= nums[j]
                j += 1
            i += 1
            result.append(product)
        return result
        