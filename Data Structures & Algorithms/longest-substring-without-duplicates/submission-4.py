class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        string = ""
        count = 0
        res = 0
        while i < len(s):
            while j < len(s) and len(set(s[i:j + 1])) == len(s[i:j + 1]):
                if len(s[i:j + 1]) > res:
                    res = len(s[i:j + 1])
                j += 1
            i += 1
        return res
            