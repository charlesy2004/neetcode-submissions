class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i  = 0
        res = 0
        for j in range(len(s)):
            if s[j] not in seen:
                seen[s[j]] = j
            else:
                i = max(i, seen[s[j]] + 1)
                seen[s[j]] = j
            res = max(j-i+1, res)
        return res
