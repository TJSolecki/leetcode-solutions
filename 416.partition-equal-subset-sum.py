class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = set([0])

        for i in range(len(nums) - 1, -1, -1):
            tempDP = set()
            for val in dp:
                if val + nums[i] == target:
                    return True
                tempDP.add(val + nums[i])
                tempDP.add(val)

            dp = tempDP

        return target in dp
