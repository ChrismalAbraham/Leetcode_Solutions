class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            N = len(subsets)
            for i in range(N):
                new_subset = list(subsets[i])
                new_subset.append(num)
                subsets.append(new_subset)
        return subsets