# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper):
            # Empty tree is valid
            if not node:
                return True
                
            # Check if current node violates bounds
            if not (lower < node.val < upper):
                return False
                
            # Check left subtree: all values must be < node.val
            # So upper bound becomes node.val
            left_valid = helper(node.left, lower, node.val)
                
            # Check right subtree: all values must be > node.val
            # So lower bound becomes node.val
            right_valid = helper(node.right, node.val, upper)
                
            return left_valid and right_valid
            
        return helper(root, float("-inf"), float("inf"))