class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp: dict[tuple[str, str], bool] = {}

        def dfs(i: int, str1: str, str2: str) -> bool:
            if (str1, str2) in dp:
                return dp[(str1, str2)]
            if i >= len(s3) and str1 == "" and str2 == "":
                return True
            elif i >= len(s3):
                return False

            res = False
            if len(str1) > 0 and str1[0] == s3[i]:
                res = res or dfs(i + 1, str1[1:], str2)

            if len(str2) > 0 and str2[0] == s3[i]:
                res = res or dfs(i + 1, str1, str2[1:])

            dp[(str1, str2)] = res
            return res

        return dfs(0, s1, s2)
