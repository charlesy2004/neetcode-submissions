class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sums = 0
        n = len(nums) - 1
        high = n
        low = 1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low