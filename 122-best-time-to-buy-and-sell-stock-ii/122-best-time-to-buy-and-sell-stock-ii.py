class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        
        profit = 0
        while sell < len(prices):
            if prices[sell] <= prices[sell - 1]:
                profit += (prices[sell - 1] - prices[buy])
                buy = sell
            sell += 1
        return profit + prices[sell - 1] - prices[buy]
                