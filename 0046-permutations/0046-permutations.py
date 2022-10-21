class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find_permutations(res, index, curr_permutation, nums):
            if index == len(nums):
                res.append(curr_permutation)
            else:
                for j in range(len(curr_permutation) + 1):
                    new_permutation = list(curr_permutation)
                    new_permutation.insert(j, nums[index])
                    find_permutations(res, index + 1, new_permutation, nums)
        res = []
        find_permutations(res, 0, [], nums)
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
        
        