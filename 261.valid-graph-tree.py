from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        visited = set()

        def dfs(node, last_node) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for child in adjacency_list[node]:
                if child != last_node and not dfs(child, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
