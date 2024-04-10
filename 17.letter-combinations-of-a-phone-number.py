class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        res = []
        num_to_chars = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        def backtrack(i: int, curr: str):
            if i == len(digits):
                res.append(curr)
                return

            n = int(digits[i])
            for c in num_to_chars[n]:
                backtrack(i + 1, curr + c)

        backtrack(0, "")
        return res
