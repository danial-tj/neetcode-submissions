# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))


        #pre-order list: [3,9,20,15,7]
        #inorder list: [9,3,15,20,7]

        #first step
        #we pass an infinite number to the dfs func
        #we have two vars preIdx and inIdx with values zero
        #then first if condition 
        #then second if condition checking if the inorder value we are at equals the limit
        #guessing it's the root so if it equals we move tthe inIdx
        #we make a root node value at preorder (first value in the preorder is the root of a tree)
        #then we increase the preIdx which is for preorder obv
        #then obv we need to add the right and left node of this root we created
        #for left node we passed root.val as the limit why is that?
        #limit was checking the value of inorder[inIdx]
        #





