class Solution(object):
    def zigzagLevelOrder(self, root):
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

        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse() 
        return res