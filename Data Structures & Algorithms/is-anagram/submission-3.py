class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
        for j in range(len(t)):
            tdict[t[j]] = tdict.get(t[j], 0) + 1
        return sdict == tdict

        