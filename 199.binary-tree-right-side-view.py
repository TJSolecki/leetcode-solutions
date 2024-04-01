from collections import deque

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res = []
        # bfs and take the max of each depth and add to res
        queue = deque()
        queue.appendleft(root)
        while queue:
            curr = None
            for _ in range(len(queue)):
                curr = queue.pop()
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            if curr:
                res.append(curr.val)

        return res
