from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        deq = deque()
        l = r = 0
        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()

            if deq and deq[0] < l:
                deq.popleft()

            deq.append(r)

            if r + 1 >= k:
                res.append(nums[deq[0]])
                l += 1
            r += 1

        return res
