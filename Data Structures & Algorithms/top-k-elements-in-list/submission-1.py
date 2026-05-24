class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adict = {}
        for num in nums:
            adict[num] = 1 + adict.get(num, 0)
        atuple = tuple(adict.items())
        alist = list(sorted(atuple, key = lambda x: x[1], reverse=True))
        return [x[0] for x in alist][:k]

        #{1:1, 2:2, 3:3}
        