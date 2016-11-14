# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root:
            return self.solve(root)
        else:
            return 0
        
    def solve(self, root):
        if root.right and root.left:
            return 1 + max(self.solve(root.right), self.solve(root.left))
            
        elif root.right:
            return 1 + self.solve(root.right)
            
        elif root.left:
            return 1 + self.solve(root.left)
        
        else:
            return 1
        