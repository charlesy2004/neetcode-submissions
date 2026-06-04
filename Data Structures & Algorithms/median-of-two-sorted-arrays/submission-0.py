class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        sorted_nums = sorted(nums1)
        if len(sorted_nums) % 2 == 0:
            return float(sorted_nums[len(sorted_nums)//2 - 1] + sorted_nums[len(sorted_nums)//2 ]) / 2
        return sorted_nums[(len(sorted_nums)//2)]
        
        