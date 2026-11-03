# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        
        res = []
        
        def level(node, depth):
            if node is None:
                return

            if depth == len(res):
                res.append([])
            
            res[depth].append(node.val)
            
            level(node.left, depth + 1)
            level(node.right, depth + 1)
        
        level(root, 0)
        res=res[::-1]
        return res
