# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def traverse_paths(root, target_sum, prefix_sum_map, path_sum):
            if root is None:
                return 0
            valid_paths = 0
            path_sum += root.val

            if target_sum == path_sum:
                valid_paths += 1

            # add to valid paths the amount of times target_sum appears in the paths skipped
            valid_paths += prefix_sum_map[path_sum - target_sum]

            # add the occurence of this path_sum to our map
            prefix_sum_map[path_sum] += 1

            valid_paths += traverse_paths(root.left,
                                          target_sum, prefix_sum_map, path_sum)
            valid_paths += traverse_paths(root.right,
                                          target_sum, prefix_sum_map, path_sum)

            # take out the occurence of this path_sum from the map for backtraking because it's not in the path anymore
            prefix_sum_map[path_sum] -= 1
            return valid_paths

        prefix_sum_map = defaultdict(int)
        return traverse_paths(root, target_sum, prefix_sum_map, 0)