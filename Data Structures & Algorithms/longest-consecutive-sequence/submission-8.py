class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted_nums = sorted(nums)
        # count = 1
        # max_cnt = 1
        # i = 1
        # while i < len(nums):
        #     if sorted_nums[i] - sorted_nums[i-1] == 1:
        #         count += 1
        #     if count > max_cnt:
        #         max_cnt = count
        #     elif sorted_nums[i] - sorted_nums[i-1] > 1:

        #         count = 1
        #     i += 1
        # if nums == []:
        #     return 0
        # return max_cnt
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest

