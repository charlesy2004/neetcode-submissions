class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)
        s2_dict = {}
        i = 0
        for j in range(len(s2)):
            s2_dict[s2[j]] = 1 + s2_dict.get(s2[j], 0)
            curr_wind_len = j - i + 1
            if curr_wind_len > len(s1):
                if s2_dict[s2[i]] > 1:
                    s2_dict[s2[i]] -= 1
                else:
                    s2_dict.pop(s2[i])
                i += 1
            if s1_dict == s2_dict:
                return True
        return False
        
                