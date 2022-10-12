# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        def find_path_sums(root, target_sum, path_arr, res):
            if root == None:
                return

            path_arr.append(root.val)
            if root.val == target_sum and not root.left and not root.right:
                # the reason why its list is because you want to append a copy not a reference to the actual array
                res.append(list(path_arr))

            find_path_sums(root.left, target_sum - root.val, path_arr, res)
            find_path_sums(root.right, target_sum - root.val, path_arr, res)

            del path_arr[-1]

        if root is None:
            return []
        res = []
        find_path_sums(root, target_sum, [], res)
        return res