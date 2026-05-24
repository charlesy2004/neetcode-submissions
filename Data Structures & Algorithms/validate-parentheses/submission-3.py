class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cdict = {")":"(", "]": "[", "}":"{"}
        for char in s:
            if char in cdict:
                if len(stack) > 0 and stack[-1] == cdict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) < 1

