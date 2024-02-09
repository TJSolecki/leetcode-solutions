class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        nums_set = set(nums)

        for num in nums_set:
            if not nums_set.__contains__(num - 1):
                len = 1
                max_len = max(len, max_len)
                next = num + 1
                while nums_set.__contains__(next):
                    len += 1
                    max_len = max(len, max_len)
                    next += 1

        return max_len
