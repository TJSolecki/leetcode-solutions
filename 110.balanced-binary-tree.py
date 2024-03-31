from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return (True, 0)
            is_left_balanced = dfs(node.left)
            is_right_balanced = dfs(node.right)
            if not is_right_balanced[0] or not is_left_balanced[0]:
                return (False, 0)
            depth = 1 + max(is_left_balanced[1], is_right_balanced[1])
            if abs(is_left_balanced[1] - is_right_balanced[1]) <= 1:
                return (True, depth)

            return (False, depth)

        return dfs(root)[0]
