class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # adict = {}
        # for num in nums:
        #     adict[num] = 1 + adict.get(num, 0)
        # atuple = tuple(adict.items())
        # alist = list(sorted(atuple, key = lambda x: x[1], reverse=True))
        # return [x[0] for x in alist][:k]

        # Note frequency questions use bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # freq = [[], [1], [2], [3]]
        #{1:1, 2:2, 3:3}
        