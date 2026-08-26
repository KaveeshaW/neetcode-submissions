class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
        left, right = 0, 1
        max = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if max < profit:
                max = profit
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max