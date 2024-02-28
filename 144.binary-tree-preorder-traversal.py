# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        curr = root
        while curr or stack:
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
            curr = stack.pop()
            while stack and not curr:
                curr = stack.pop()

        return res
