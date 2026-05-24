class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in range(len(numbers)):
            complement = target - numbers[num]
            n = 1
            if complement in numbers[num + 1:]:
                while numbers[num + n] != complement:
                    n += 1
                return [num + 1, num + n + 1]
        return []