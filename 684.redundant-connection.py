from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # Finds the parent for the given node
        def find(node: int) -> int:
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(node_1: int, node_2: int) -> bool:
            parent_1, parent_2 = find(node_1), find(node_2)
            if parent_1 == parent_2:
                return False

            if rank[parent_1] > rank[parent_2]:
                par[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                par[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            return True

        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return [node_1, node_2]
