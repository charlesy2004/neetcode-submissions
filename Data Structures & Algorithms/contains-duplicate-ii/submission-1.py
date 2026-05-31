class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        while i < len(nums):
            j = i 
            while j < len(nums):
                if nums[i] == nums[j] and j - i <= k and i != j:
                    return True
                j += 1
            i += 1
        return False
        