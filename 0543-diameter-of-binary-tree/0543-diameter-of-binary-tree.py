class Solution(object):
    def diameterOfBinaryTree(self, root):

        ans = [0]

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            ans[0] = max(ans[0], left + right)

            return 1 + max(left, right)

        height(root)

        return ans[0]