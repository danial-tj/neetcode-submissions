# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()

        queue.append(root)

        res = []

        while queue:
            level_size = len(queue)

            level_element = []
            for i in range(level_size):
                curr = queue.popleft()
                level_element.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        #when do we know we are on the next level? when the queue is
        #empty ?
            res.append(level_element)


        return res

        
        