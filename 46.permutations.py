class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            num = nums.pop(0)
            permutations = self.permute(nums)
            for permutation in permutations:
                permutation.append(num)
            res.extend(permutations)
            nums.append(num)

        return res
