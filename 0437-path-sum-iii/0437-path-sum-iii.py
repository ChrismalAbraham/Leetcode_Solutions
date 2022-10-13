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

            valid_paths = 0
            if root.val == target_sum:
                valid_paths += 1
            for i in range(len(nums_to_add)):
                if target_sum == nums_to_add[i] + root.val:
                    valid_paths += 1
                nums_to_add[i] += root.val

            nums_to_add.append(root.val)
            left_subtree_valid_paths = traverse_paths(
                root.left, target_sum, nums_to_add)
            right_subtree_valid_paths = traverse_paths(
                root.right, target_sum, nums_to_add)

            del nums_to_add[-1]
            for i in range(len(nums_to_add)):
                nums_to_add[i] -= root.val

            return valid_paths + left_subtree_valid_paths + right_subtree_valid_paths

        if root is None:
            return 0

        return traverse_paths(root, targetSum, [])