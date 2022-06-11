class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        If buy price is less than the sell price, sell it.
        Otherwise buy it at the sell price.
        '''
        
        buy, mx_profit = 0, 0
        
        for sell in range(1, len(prices) ):
            mx_profit += prices[sell] - prices[buy] if prices[sell] - prices[buy] > 0 else 0
            buy = sell
            
        return mx_profit