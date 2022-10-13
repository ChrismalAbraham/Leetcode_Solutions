# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, c_sum):
            if not node: return
            
            c_sum += node.val
            self.result += prefix_sum[c_sum - targetSum]
            prefix_sum[c_sum] += 1
            
            preorder(node.left, c_sum)
            preorder(node.right, c_sum)
            
            prefix_sum[c_sum] -= 1
            # c_sum -= node.val
            
            
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        self.result = 0
        
        preorder(root, 0)
        return self.result