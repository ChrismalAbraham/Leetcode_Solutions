# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findMaxDiameter(self, node) -> int:
            if node == None: return 0
            
            left_max = findMaxDiameter(self, node.left)
            right_max = findMaxDiameter(self, node.right)
            
            self.max_diameter = max(self.max_diameter, left_max + right_max)
            
            return 1 + max(left_max, right_max)
            
        self.max_diameter = 0
        findMaxDiameter(self, root)
        return self.max_diameter