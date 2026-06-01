class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        min_diff = float("inf")
        for i in range(len(nums) - k + 1):
            curr_diff = sorted_nums[i + k - 1] - sorted_nums[i]
            min_diff = min(min_diff, curr_diff)
        return min_diff

                
