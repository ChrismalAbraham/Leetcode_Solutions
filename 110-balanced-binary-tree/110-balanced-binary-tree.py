# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isSubTreeBalanced(node):
            if node == None:
                return [True, 0]
            left_check = isSubTreeBalanced(node.left)
            right_check = isSubTreeBalanced(node.right)
            height = 1 + max(left_check[1], right_check[1])
            if left_check[0] and right_check[0] and abs(left_check[1] - right_check[1]) < 2:
                return [True, height]
            else:
                return [False, height]
        return isSubTreeBalanced(root)[0]
            