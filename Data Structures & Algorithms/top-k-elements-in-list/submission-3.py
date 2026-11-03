class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        minh = []
        for i, num in enumerate(nums):
            freq[num] = 1 + freq.get(num, 0)
        for num, cnt in freq.items():
            heapq.heappush(minh, (cnt, num))
            if len(minh) > k:
                heapq.heappop(minh)
        res = []
        for j, (c, n) in enumerate(minh):
            res.append(n)
        
        return res
        # freq = [[], [1], [2], [3]]
        #{1:1, 2:2, 3:3}
        