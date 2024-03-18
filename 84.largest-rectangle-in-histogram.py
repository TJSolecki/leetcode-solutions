class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[tuple[int, int]] = []
        max_height = 0
        for i, height in enumerate(heights):
            start_i = i
            while stack and stack[-1][1] > height:
                popped_index, popped_height = stack.pop()
                max_height = max(max_height, (i - popped_index) * popped_height)
                start_i = popped_index
            stack.append((start_i, height))

        while stack:
            popped_index, popped_height = stack.pop()
            max_height = max(max_height, (len(heights) - popped_index) * popped_height)

        return max_height
