class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        # while i < len(nums):
        #     j = 0
        #     product = 1
        #     while j < len(nums):
        #         if j != i:
        #             product *= nums[j]
        #         j += 1
        #     i += 1
        #     result.append(product)
        # return result
        res = [0] * len(nums)
        prod = 1
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            if nums[i] == 0:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
            if zero_cnt == 1:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else: 
                res[i] = prod // nums[i]
        return res
