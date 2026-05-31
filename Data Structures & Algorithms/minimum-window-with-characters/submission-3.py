class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_dict = {}
        for char in t:
            freq_dict[char] = 1 + freq_dict.get(char, 0)
        need = len(freq_dict)
        have = 0
        l = 0
        r = 0
        s_dict = {}
        current_str = ""
        best_len = float("inf")
        while r < len(s):
            s_dict[s[r]] = 1 + s_dict.get(s[r], 0)
            if s[r] in freq_dict and s_dict.get(s[r], 0) == freq_dict[s[r]]:
                have += 1
            while have == need:
                if len(s[l:r+1]) < best_len:
                    best_len = len(s[l:r+1])
                    current_str = s[l:r+1]
                if s_dict[s[l]] > 1:
                    s_dict[s[l]] -= 1
                else:
                    s_dict.pop(s[l])
                if s[l] in freq_dict and s_dict.get(s[l], 0) < freq_dict[s[l]]:
                    have -= 1
                l += 1
                
            r += 1
        return current_str
            
        
        
        
    

            
