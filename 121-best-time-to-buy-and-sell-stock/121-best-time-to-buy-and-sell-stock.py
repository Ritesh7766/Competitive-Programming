class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, buy = len(prices), 0
        
        mx_profit = 0
        for sell in range(1, n):
            while prices[buy] > prices[sell]: buy += 1
            mx_profit = max(mx_profit, prices[sell] - prices[buy])
        return mx_profit
        
        