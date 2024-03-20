from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res

        def get_num_hours(k: int):
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / k)
            return total_hours

        while l <= r:
            mid = (l + r) // 2
            total_hours = get_num_hours(mid)
            if total_hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
