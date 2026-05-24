class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        for i in range(len(temperatures)):
            k = i + 1
            count = 1
            while k < len(temperatures):
                if temperatures[k] > temperatures[i]:
                    break
                count += 1
                k += 1
            if k == len(arr):
                arr[i] = 0
            else:    
                arr[i] = count
        return arr
