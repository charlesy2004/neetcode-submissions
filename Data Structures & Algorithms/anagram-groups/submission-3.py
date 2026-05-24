class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in adict:
                adict[tuple(count)] = [s]
            else:
                adict[tuple(count)].append(s)
        # print(adict.values())
        # return []
        return list(adict.values())


# adict = {a:1, c:1. t:1}