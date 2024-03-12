class Solution:
    def trap(self, height: list[int]) -> int:
        max_l = height[0]
        max_r = height[-1]
        l = 0
        r = len(height) - 1
        trapped = 0
        while l < r:
            if max_l <= max_r:
                l += 1
                rain_trapped = max_l - height[l]
                if rain_trapped > 0:
                    trapped += rain_trapped
                max_l = max(max_l, height[l])
            else:
                r -= 1
                rain_trapped = max_r - height[r]
                if rain_trapped > 0:
                    trapped += rain_trapped
                max_r = max(max_r, height[r])

        return trapped
