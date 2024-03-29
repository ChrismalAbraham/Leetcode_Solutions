# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.left is None: return 1 + self.minDepth(root.right)
        if root.right is None: return 1 + self.minDepth(root.left)
        minimum_depth = min(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + minimum_depth
         
# Breadth first search solution using deque
#         if root is None:
#             return 0

#         queue = deque()
#         queue.append(root)
#         min_depth = 1
#         while queue:
#             level_len = (len(queue))
#             for _ in range(level_len):
#                 node = queue.popleft()
#                 if node.right is None and node.left is None:
#                     return min_depth

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             min_depth += 1
#         return min_depth