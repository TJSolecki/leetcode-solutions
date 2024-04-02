# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0

        def dfs(node: Optional[TreeNode], curr_max):
            nonlocal num_good_nodes
            if not node:
                return
            if curr_max <= node.val:
                num_good_nodes += 1
            new_max = max(node.val, curr_max)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, float("-inf"))
        return num_good_nodes
