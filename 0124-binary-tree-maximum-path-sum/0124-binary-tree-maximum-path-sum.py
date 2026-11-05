class Solution(object):
    def maxPathSum(self, root):
        maxi = [float('-inf')]

        def solve(node):
            if node is None:
                return 0

            lsum = max(0, solve(node.left))
            rsum = max(0, solve(node.right))
            curr = node.val + lsum + rsum

            maxi[0] = max(maxi[0], curr)
            return node.val + max(lsum, rsum)

        solve(root)
        return maxi[0]