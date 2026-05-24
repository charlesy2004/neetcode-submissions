class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max = 0
        while (j < (len(prices))):
            current = 0
            if prices[i] <= prices[j]:
                current =  prices[j] - prices[i]
                j += 1
            else:
                i = j
                j += 1
            if current > max:
                max = current
            
        # for i in range(len(prices)):
        #     buy = prices[i]

        return max