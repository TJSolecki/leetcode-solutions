class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            max_lis = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_lis = max(max_lis, dp[j] + 1)

            dp[i] = max_lis

        return max(dp)
