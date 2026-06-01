class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for char in s:
            if char in char_dict:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                test = stack.pop()
                if char_dict[test] != char:
                    return False
        return len(stack) == 0
        
        

