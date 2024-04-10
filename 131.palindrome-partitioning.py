class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s: str):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res: list[list[str]] = []
        partition: list[str] = []

        def backtrack(i: int, last_is_pal: bool):
            if i == len(s):
                if not last_is_pal:
                    return
                res.append(partition[:])
                return

            if len(partition) == 0:
                partition.append(s[i])
                backtrack(i + 1, True)
            elif last_is_pal:
                partition.append(s[i])
                backtrack(i + 1, True)

                partition.pop()
                partition[-1] = partition[-1] + s[i]
                backtrack(i + 1, is_pal(partition[-1]))
            else:
                partition[-1] = partition[-1] + s[i]
                backtrack(i + 1, is_pal(partition[-1]))

        backtrack(0, False)
        return res
