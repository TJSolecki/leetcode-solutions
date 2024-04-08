class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def dfs(curr: list[int], i: int):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(curr, i + 1)

        dfs([], 0)

        return res
