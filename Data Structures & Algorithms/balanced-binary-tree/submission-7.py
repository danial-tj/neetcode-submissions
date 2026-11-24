# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:       
        #at each root check the diff between left and right height
        #define one more function

        if not root:
            return True
        
        stack = [root]
        mp = {None: (True,0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftValid, leftHeight = mp[node.left]
                rightValid, rightHeight = mp[node.right]
                mp[node] = (leftValid and rightValid and abs(leftHeight - rightHeight) <= 1, 1+ max(leftHeight, rightHeight))

                
                

        return mp[root][0]

