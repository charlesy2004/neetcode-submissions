class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = {}
        for str1 in strs:
            c_arr = [0] * 26
            alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
            for char in str1:
                c_arr[ord(char)-ord('a')] += 1
            key = tuple(c_arr)
            if key in adict:
                adict[key].append(str1)
            else:
                adict[key] = []
                adict[key].append(str1)
        return list(adict.values())

            

