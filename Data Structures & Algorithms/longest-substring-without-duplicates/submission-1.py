class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            j = i + 1
            str1 = s[i]
            while j < len(s) and s[j]  not in str1:
                str1 += s[j]
                j += 1
            if len(str1) > max:
                max = len(str1)
        return max