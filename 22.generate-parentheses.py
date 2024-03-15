class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        max_len = n * 2
        res = []
        self.open: int = 1
        self.closed = 0

        def dfs(curr_str: str):
            if len(curr_str) == max_len:
                res.append(curr_str)
                return
            if curr_str == "":
                curr_str = "("
                self.open = 1

            if self.closed < self.open:
                self.closed += 1
                dfs(curr_str + ")")
                self.closed -= 1

            if self.open < n:
                self.open += 1
                dfs(curr_str + "(")
                self.open -= 1

        dfs("(")
        return res
