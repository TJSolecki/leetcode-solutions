class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start, end, max_profit = 0, 0, 0
        for i in range(1, len(prices)):
            if prices[i] > prices[start]:
                end = i
            else:
                start = end = i

            max_profit = max(max_profit, prices[end] - prices[start])

        return max_profit
