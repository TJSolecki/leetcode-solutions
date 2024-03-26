class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(curr, i):
            if i >= len(nums):
                res.append(curr)
                return
            dfs(curr + [nums[i]], i + 1)
            dfs(curr, i + 1)

        dfs([], 0)

        return res
