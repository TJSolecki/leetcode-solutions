class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mem = [0 for _ in range(26)]
        l, max_len = 0, 0

        for r in range(len(s)):
            mem[ord(s[r]) - 65] += 1

            if r - l + 1 - max(mem) <= k:
                max_len = max(max_len, r - l + 1)
            else:
                while r - l + 1 - max(mem) > k:
                    mem[ord(s[l]) - 65] -= 1
                    l += 1

        return max_len
