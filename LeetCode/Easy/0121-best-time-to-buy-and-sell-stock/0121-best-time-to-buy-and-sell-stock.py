class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_profit = 0
        for i in prices:
            if i < lowest:
                lowest = i
            today_profit = i - lowest
            if today_profit > best_profit:
                best_profit = today_profit 
        return best_profit