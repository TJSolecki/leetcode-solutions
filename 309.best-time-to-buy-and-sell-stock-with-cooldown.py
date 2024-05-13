class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1, -1] for _ in range(len(prices))]

        def dfs(i: int, buying: int) -> int:
            if i >= len(prices):
                return 0

            if dp[i][buying] != -1:
                return dp[i][buying]
            cooldown = dfs(i + 1, buying)
            if buying == 1:
                dp[i][buying] = max(dfs(i + 1, 0) - prices[i], cooldown)
                return dp[i][buying]
            else:
                dp[i][buying] = max(dfs(i + 2, 1) + prices[i], cooldown)
                return dp[i][buying]

        return dfs(0, 1)
