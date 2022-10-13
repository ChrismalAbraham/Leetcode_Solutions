# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse_paths(root, target_sum, nums_to_add):
            if root is None:
                return 0

            nums_to_add.append(root.val)
            valid_paths, path_sum = 0, 0

            for i in range(len(nums_to_add) - 1, -1, -1):
                path_sum += nums_to_add[i]
                if path_sum == target_sum:
                    valid_paths += 1

            valid_paths += traverse_paths(
                root.left, target_sum, nums_to_add)
            valid_paths += traverse_paths(
                root.right, target_sum, nums_to_add)

            del nums_to_add[-1]

            return valid_paths

        if root is None:
            return 0

        return traverse_paths(root, targetSum, [])