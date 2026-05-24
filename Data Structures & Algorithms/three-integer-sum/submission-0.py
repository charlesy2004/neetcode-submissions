class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        alist = []
        for index, i in enumerate(nums):
            if i > 0:
                break
            else:
                target = -i
                j = index + 1
                k = len(nums) - 1
                while (j < k):
                    if (nums[j] + nums[k]) > target:
                        k-=1
                    elif (nums[j] + nums[k]) < target:
                        j += 1
                    else:
                        if [i, nums[j], nums[k]] not in alist:
                            alist.append([i, nums[j], nums[k]])
                        j += 1
                        k -= 1
        return alist
                

