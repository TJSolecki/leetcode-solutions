class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ""
        longest_len = 0
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if (end - start + 1) > longest_len:
                    longest_pal = s[start : end + 1]
                    longest_len = len(longest_pal)
                start -= 1
                end += 1

            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if (end - start + 1) > longest_len:
                    longest_pal = s[start : end + 1]
                    longest_len = len(longest_pal)
                start -= 1
                end += 1

        return longest_pal
