# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def count_paths_prefix_sum(current_node, target_sum, map, current_path_sum):
            if current_node is None:
                return 0

            path_count = 0

            current_path_sum += current_node.val

            if target_sum == current_path_sum:
                path_count += 1

            path_count += map[current_path_sum - target_sum]

            map[current_path_sum] = map[current_path_sum] + 1

            path_count += count_paths_prefix_sum(current_node.left, target_sum, map, current_path_sum)
            path_count += count_paths_prefix_sum(current_node.right, target_sum, map, current_path_sum)
            
            #value_to_deduct = map[current_path_sum] if map[current_path_sum] else 1
            map[current_path_sum] = map[current_path_sum] - 1

            return path_count
        
        map = defaultdict(int)

        return count_paths_prefix_sum(root, target_sum, map, 0)