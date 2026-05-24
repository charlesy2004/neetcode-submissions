class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        adict = {}
        l = 0
        res = 0
        for r in range(len(s)):
            adict[s[r]] = adict.get(s[r], 0) + 1
            if (r-l+1) - max(adict.values()) > k:
                adict[s[l]] -= 1
                l += 1
            
            if r-l+1 > res:
                res = r-l+1
        return res




        # curr_k = 0
        # res = 0
        # curr = 0
        # marker = []
        # j = 0
        # for i in range(len(s)):
        #     if s[i] != most_common and curr_k < k:
        #         curr_k += 1
        #         marker.append(i)
        #     elif s[i] != most_common and curr_k >= k:
        #         while j <= marker[0]:
        #             j+=1
        #         curr = 0
        #         marker = []
        #         curr_k = 0
        #     curr += 1
        #     if curr > res:
        #         res = curr
        # curr_k = 0

        # return res

                



            
        