class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max1 = 0
        for num in num_set:
            if (num - 1) not in num_set:
                n = 1
                while num + n in num_set:
                    n += 1
                if n > max1:
                    max1 = n
        return max1

        
