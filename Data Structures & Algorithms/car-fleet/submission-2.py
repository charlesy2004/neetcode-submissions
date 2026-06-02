class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        sorted_arr = sorted(arr, key = lambda x: x[0], reverse = True)

        for i in range(len(sorted_arr)):
            time = (target - sorted_arr[i][0])/sorted_arr[i][1]
            if stack == []:
                stack.append((sorted_arr[i], time))
            if time > stack[-1][1]:
                stack.append((sorted_arr[i], time))
        return len(stack)

        


