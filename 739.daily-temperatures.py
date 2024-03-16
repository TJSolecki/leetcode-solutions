class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and stack[-1][0] < curr_temp:
                (_, popped_index) = stack.pop()
                res[popped_index] = i - popped_index
            stack.append((curr_temp, i))

        return res
