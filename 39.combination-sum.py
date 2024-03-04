class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def add_solutions(i: int, vals: list[int], sum_of_vals: int = 0):
            if i == len(candidates):
                return
            if sum_of_vals > target:
                return
            elif sum_of_vals == target:
                res.append(vals)
                return
            add_solutions(i, vals + [candidates[i]], sum_of_vals + candidates[i])
            add_solutions(i + 1, vals, sum_of_vals)

        add_solutions(0, [])
        return res
