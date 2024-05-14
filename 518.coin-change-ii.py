class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        def dfs(i: int, total: int) -> int:
            if total == 0:
                return 1
            elif i < 0:
                return 0
            if dp[i][total] != -1:
                return dp[i][total]
            res = 0
            if coins[i] <= total:
                res += dfs(i, total - coins[i])
            res += dfs(i - 1, total)
            dp[i][total] = res
            return res

        return dfs(len(coins) - 1, amount)
