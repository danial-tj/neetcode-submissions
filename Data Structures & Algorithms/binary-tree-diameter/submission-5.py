# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #at each node  we measure what is the depth we got and we plust them to get the diameter

        if not root:
            return 0


        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)

            return 1+ max(left,right)

        #at each level
        dfs(root)
        return res
