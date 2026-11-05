from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        queue.appendleft(root)
        output = []

        traversed = []

        if root is None:
            return []
        while queue:
            level = []
            size = len(queue)
            
            for _ in range(size):
                curr = queue.pop()
                level.append(curr.val)

                if curr.left is not None:
                    queue.appendleft(curr.left)

                if curr.right is not None:
                    queue.appendleft(curr.right)

            traversed.append(level)

        return traversed




