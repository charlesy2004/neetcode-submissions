class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            new_val = max(x,y) - min(x,y)
            if new_val != 0:
                heapq.heappush_max(stones, new_val)
            heapq.heapify_max(stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

        