class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_taken = [0] * len(nums)
        max_taken[0] = nums[0]
        max_taken[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            max_taken[i] = max(nums[i] + max_taken[i - 2], max_taken[i - 1])

        return max(max_taken[-1], max_taken[-2])
