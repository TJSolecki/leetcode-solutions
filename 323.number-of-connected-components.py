from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        visited = set()
        visited_local = set()
        adjacent_list = defaultdict(list)
        for node_1, node_2 in edges:
            adjacent_list[node_1].append(node_2)
            adjacent_list[node_2].append(node_1)

        def dfs(node) -> bool:
            if node in visited:
                return False
            visited_local.add(node)
            for neighbor in adjacent_list[node]:
                if neighbor not in visited_local and not dfs(neighbor):
                    return False

            visited.add(node)
            return True

        res = 0
        for node in range(n):
            visited_local = set()
            if dfs(node):
                res += 1
        return res
