class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_prof = 0
        min_buy = prices[i]
        while i < len(prices):
            if prices[i] < min_buy:
                min_buy = prices[i]
            current_prof = prices[i] - min_buy
            if current_prof > max_prof:
                max_prof = current_prof
            i += 1
        return max_prof
            
            


        