class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp: dict[tuple[int, int], int] = {}

        def dfs(i: int, total: int) -> int:
            if (i, total) in dp:
                return dp[(i, total)]
            if i >= len(nums):
                return 1 if total == target else 0
            dp[(i, total)] = dfs(i + 1, total - nums[i]) + dfs(i + 1, total + nums[i])
            return dp[(i, total)]

        return dfs(0, 0)
