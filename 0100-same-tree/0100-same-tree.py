# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def tree(root, res):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            tree(root.left, res)
            tree(root.right, res)

        res1, res2 = [], []
        tree(p, res1)
        tree(q, res2)
        return res1 == res2

        