class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()
        for num in nums:
            hset.add(num)
        return len(hset) !=len(nums)
