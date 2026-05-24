class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        if h == len(piles):
            return max(piles)
        min_k = 1
        max_k = max(piles)
        k = 0
        while min_k <= max_k:
            k = (min_k + max_k)//2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/k)
            if total <= h:
                max_k = k - 1
            elif total > h:
                min_k = k + 1
        return min_k
            
