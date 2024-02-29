# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def build_inorder(self, root):
        stack = []
        curr = root
        inorder = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder

    def build_preorder(self, root):
        if not root:
            return []
        curr = None
        stack = [root]
        preorder = []

        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return preorder

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        preorder = self.build_preorder(root)
        inorder = self.build_inorder(root)

        preorder_str = ""
        inorder_str = ""
        for i in range(len(preorder)):
            preorder_str += str(preorder[i]) + ","
            inorder_str += str(inorder[i]) + ","

        preorder_str = preorder_str[:-1]
        inorder_str = inorder_str[:-1]

        return preorder_str + "|" + inorder_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "|":
            return None
        orders = data.split("|")
        preorder_str = orders[0]
        inorder_str = orders[1]
        preorder = list(map(int, preorder_str.split(",")))
        inorder = list(map(int, inorder_str.split(",")))

        def build_tree(preorder, inorder):
            if not preorder:
                return None
            val = preorder[0]
            mid = inorder.index(val)
            node = TreeNode(val)
            node.right = build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
            node.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
            return node

        return build_tree(preorder, inorder)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
