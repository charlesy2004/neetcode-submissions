class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max = 0
        for num in num_set:
            if (num - 1) not in nums:
                n = 1
                while num + n in num_set:
                    n += 1
                if n > max:
                    max = n
        return max
