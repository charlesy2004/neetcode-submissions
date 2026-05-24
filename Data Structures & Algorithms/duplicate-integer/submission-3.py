class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False