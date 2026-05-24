class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in adict:
                return [adict[complement], index]
            adict[num] = index
        return []