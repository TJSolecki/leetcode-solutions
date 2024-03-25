class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_diameter
