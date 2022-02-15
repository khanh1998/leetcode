from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        length = len(prices)
        buy = 0
        sell = 1
        max_profit = 0
        while sell < length:
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            if profit < 0:
                buy = sell
            sell += 1
        return max_profit
            