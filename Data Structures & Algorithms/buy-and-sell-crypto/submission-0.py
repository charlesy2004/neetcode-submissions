class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices) - 1):
            j =  i + 1            
            while (j < len(prices)):
                current = prices[j] - prices[i]
                if current > max:
                    max = current
                j += 1
        return max