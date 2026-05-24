class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arr = []
        stack = []
        for i in range(n):
            arr.append((position[i], speed[i]))
        sorted_data = sorted(arr, key=lambda item: item[0], reverse=True)
        for i in range(n):
            time = (target - sorted_data[i][0])/sorted_data[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


