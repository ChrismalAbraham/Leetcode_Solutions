class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find_permutations(nums, res, curr_permutation, index):
            if index == len(nums):
                res.append(curr_permutation)
            else:
                for i in range(len(curr_permutation) + 1):
                    new_permutation = list(curr_permutation)
                    new_permutation.insert(i, nums[index])
                    find_permutations(nums, res, new_permutation, index + 1)
        
        res = []
        find_permutations(nums, res, [], 0)
        return res
        
#         res = []
#         len_nums = len(nums)
#         permutations = deque()
#         permutations.append([])
#         for num in nums:
#             len_permutations = len(permutations)
#             for i in range(len_permutations):
#                 curr_permutation = permutations.popleft()
#                 for j in range(len(curr_permutation) + 1):
#                     new_permutation = list(curr_permutation)
#                     new_permutation.insert(j, num)
#                     if len(new_permutation) == len_nums:
#                         res.append(new_permutation)
#                     else:
#                         permutations.append(new_permutation)

#         return res
        
        