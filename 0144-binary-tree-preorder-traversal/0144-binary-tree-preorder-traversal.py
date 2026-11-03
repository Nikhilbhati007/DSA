# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans=[]
        def preorder(node,ans):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left,ans)
            preorder(node.right,ans)
        preorder(root,ans)
        return ans
