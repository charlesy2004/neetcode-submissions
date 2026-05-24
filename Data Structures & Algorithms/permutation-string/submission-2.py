class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        adict = {}
        for i in s1:
            adict[i] = adict.get(i, 0) + 1
        bdict = {}
        j = 0
        for k in range(len(s2)):
            if k - j + 1 > len(s1):
                bdict[s2[j]] = bdict.get(s2[j]) - 1
                if bdict[s2[j]] == 0:
                    bdict.pop(s2[j])
                j += 1
            bdict[s2[k]] = bdict.get(s2[k], 0) + 1
            if adict == bdict:
                return True
        # for i in range(len(s2) - len(s1) + 1):
        #     bdict = {}
        #     for j in range(len(s1)):
        #         if s2[i + j] in adict:
        #             bdict[s2[i+j]] = bdict.get(s2[i + j], 0) + 1
                
        #     if adict == bdict:
        #         return True
        return False



        
                