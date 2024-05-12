class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        max_len = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1

                    max_len = max(max_len, dp[i][j])
                elif j > 0 and i > 0:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]

        return max_len
