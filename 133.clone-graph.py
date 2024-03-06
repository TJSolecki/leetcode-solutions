from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list[Optional["Node"]] = (
            neighbors if neighbors is not None else []
        )


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        cloned = {}

        def dfs(node: Optional["Node"]) -> Optional["Node"]:
            if not node:
                return None
            new_node = Node(node.val, [])
            cloned[node] = new_node
            for child in node.neighbors:
                if child and child not in cloned:
                    cloned_child = dfs(child)
                    new_node.neighbors.append(cloned_child)
                elif child and child in cloned:
                    new_node.neighbors.append(cloned[child])

            return new_node

        return dfs(node)
