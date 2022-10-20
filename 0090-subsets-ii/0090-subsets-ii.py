class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()

        for i in range(len(nums)):
            start_of_loop = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_of_loop = len_subsets
            len_subsets = len(subsets)
            for x in range(start_of_loop, len_subsets):
                subset = list(subsets[x])
                subset.append(nums[i])
                subsets.append(subset)

        return subsets
