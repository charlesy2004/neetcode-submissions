class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        result = []
        while i < len(nums) - 1:
            target = sorted_nums[i] * -1
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                i += 1
                continue
            k = i + 1
            j = len(nums) - 1
            # if i > 0:
            #     return result
            while k < j:
                if sorted_nums[k] + sorted_nums[j] < target:
                    k += 1
                elif sorted_nums[k] + sorted_nums[j] > target:
                    j -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[k], sorted_nums[j]])
                    k += 1
                    j -= 1
                    while k < j and sorted_nums[k] == sorted_nums[k-1]:
                        k += 1
                    while k < j and sorted_nums[j] == sorted_nums[j + 1]:
                        j -= 1

                
            i += 1
        return result
            
            

        