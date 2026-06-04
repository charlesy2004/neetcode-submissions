class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            curr = (l + r)//2
            if nums[curr] > nums[r]:
                l = curr + 1
            else:
                r = curr
        pivot = l
        left = 0
        right = len(nums) - 1
        while left <= right:
            curr = (left + right) // 2
            curr_pivot = (curr + pivot) % len(nums)
            if nums[curr_pivot] < target:
                left = curr + 1
            elif nums[curr_pivot] > target:
                right = curr - 1
            elif nums[curr_pivot] == target:
                return curr_pivot
        return -1



