# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            level_len = len(queue)
            level_sum = 0.0  # keep the level sum a double to get decimal average
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_len)
        return result