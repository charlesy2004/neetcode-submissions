class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b,
            "*": lambda a, b : a * b,
            "/": lambda a, b : int(a / b)
        }
        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                val_b = stack.pop()
                val_a = stack.pop()
                curr_val = operations[char](val_a, val_b)
                stack.append(curr_val)
        return stack[-1]
        