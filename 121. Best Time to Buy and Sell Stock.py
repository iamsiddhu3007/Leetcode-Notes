class Solution(object):
    def maxProfit(self, prices):
        # if not prices:
        #     return 0

        # min_price = prices[0]
        # max_profit = 0

        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit
        if not prices:
            return 0
        left = 0
        right = 1
        maxProfit = 0
        while right<len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right+=1
        return maxProfit
