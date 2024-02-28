# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        val = preorder[0]
        mid = inorder.index(val)
        left_inorder, right_inorder = inorder[:mid], inorder[mid + 1 :]
        left_preorder = preorder[1 : mid + 1]
        right_preorder = preorder[mid + 1 :]
        return TreeNode(
            preorder[0],
            self.buildTree(left_preorder, left_inorder),
            self.buildTree(right_preorder, right_inorder),
        )
