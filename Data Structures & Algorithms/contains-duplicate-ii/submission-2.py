class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        while i < len(nums):
            j = 0
            while j <= k:
                if i + j < len(nums) and nums[i] == nums[i + j] and j != 0 :
                    return True
                j += 1
            i += 1
        return False
        