class Solution:
    def findMin(self, nums: List[int]) -> int:
        minim = float("inf")
        for num in nums:
            minim = min(num, minim)
        return minim
        
