class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = {}
        for str in strs:
            cdict = {}
            for char in str:
                if char not in cdict:
                    cdict[char] = 1
                else:
                    cdict[char] += 1
            if tuple(sorted(cdict.items())) not in adict:
                adict[tuple(sorted(cdict.items()))] = [str]
            else:
                adict[tuple(sorted(cdict.items()))].append(str)
        return list(adict.values())
            

