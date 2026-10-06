# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #when you go right the node is bigger than you 
        #first thing is finding the node p and q by dfs perhaps?
        #we need to know the parents of each and the edge case is we might be given the parent
        #of one of the nodes as either p or q 
        #idea is not to hold just the value of any parent but the big ones casue most recent parent might
        #simply not be the answer 

        if not root:
            return

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        else: return root
        