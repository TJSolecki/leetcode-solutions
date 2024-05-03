class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        for i in range(len(s)):
            start, e = i, i
            while (
                start >= 0
                and start < length
                and e < length
                and e >= 0
                and s[start] == s[e]
            ):
                count += 1
                start -= 1
                e += 1

            start, e = i, i + 1
            while (
                start >= 0
                and start < length
                and e < length
                and e >= 0
                and s[start] == s[e]
            ):
                count += 1
                start -= 1
                e += 1

        return count
