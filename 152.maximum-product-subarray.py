class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        max_product = 1
        min_product = 1

        for n in nums:
            temp = max_product * n
            max_product = max(max_product * n, min_product * n, n)
            min_product = min(temp, min_product * n, n)
            res = max(max_product, res)

        return res
