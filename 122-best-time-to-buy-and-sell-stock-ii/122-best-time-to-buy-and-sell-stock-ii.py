class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        buy, mx_profit = 0, 0
        
        for sell in range(1, len(prices) ):
            mx_profit += prices[sell] - prices[buy] if prices[sell] - prices[buy] > 0 else 0
            buy = sell
            
        return mx_profit