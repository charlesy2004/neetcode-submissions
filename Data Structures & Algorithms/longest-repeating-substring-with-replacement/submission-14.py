class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        res = 0
        i = 0
        for j in range(len(s)):
            char_dict[s[j]] = 1 + char_dict.get(s[j], 0)
            window_len = j - i + 1
            most_common = max(char_dict.values())
            replacements_needed = window_len - most_common            
            if replacements_needed > k:
                char_dict[s[i]] -= 1
                i += 1
            if j - i + 1 > res:
                res = j - i + 1
            # while replacements_needed <  
        return res
            