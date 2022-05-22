class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
            mx_profit = max(mx_profit, prices[sell] - prices[buy])
            sell += 1
        return mx_profit