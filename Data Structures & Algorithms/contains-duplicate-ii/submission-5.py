class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        adict = {}
        while i < len(nums):
            if nums[i] in adict:
                if i - adict[nums[i]] <= k:
                    return True
            adict[nums[i]] = i
            i += 1
        return False
        