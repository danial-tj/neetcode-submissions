class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, 0)]  # (node, depth)
        
        while stack:
            node, depth = stack.pop()
            
            if not node:
                continue
            
            # First time seeing this depth = rightmost node at that depth
            if depth == len(res):
                res.append(node.val)
            
            # Push LEFT first, then RIGHT
            # Since stack is LIFO, RIGHT will be popped first
            # This ensures we visit right subtree before left
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        
        return res