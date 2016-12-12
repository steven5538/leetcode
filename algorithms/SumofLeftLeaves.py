# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        return self.solve(root, False)
    
    def solve(self, root, left):
        if not root:
            return 0
        if left and root.left is root.right:
            return root.val
    
        return self.solve(root.left, True) + self.solve(root.right, False)
        