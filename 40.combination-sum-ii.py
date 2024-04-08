class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        vals = []

        def add_to_solution_set(i: int, curr_sum: int):
            nonlocal vals
            if curr_sum > target:
                return
            elif curr_sum == target:
                res.append(vals[:])
                return
            if i >= len(candidates):
                return
            vals.append(candidates[i])
            add_to_solution_set(i + 1, curr_sum + candidates[i])
            vals.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            add_to_solution_set(i + 1, curr_sum)

        add_to_solution_set(0, 0)
        return res
