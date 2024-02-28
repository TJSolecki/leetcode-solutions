# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


res = 0


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = root.val

        def max_path(root):
            if not root:
                return 0
            left_max = max_path(root.left)
            right_max = max_path(root.right)

            split_max = root.val + max(left_max, 0) + max(right_max, 0)
            global res
            res = max(res, split_max)
            return max(left_max, right_max, 0) + root.val

        return max(max_path(root), res)
