# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, range=(float("infinity") * -1, float("infinity"))):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.val <= range[0] or root.val >= range[1]:
            return False

        return self.isValidBST(root.left, (range[0], root.val)) and self.isValidBST(
            root.right, (root.val, range[1])
        )
