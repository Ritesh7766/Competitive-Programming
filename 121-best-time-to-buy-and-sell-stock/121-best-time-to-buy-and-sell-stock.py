class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        mx_profit = 0
        
        for sell in range(1, len(prices) ):
            if prices[sell] <= prices[buy]:
                buy = sell
            mx_profit = max(mx_profit, prices[sell] - prices[buy])
        
        return mx_profit