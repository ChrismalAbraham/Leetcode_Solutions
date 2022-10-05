class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        for i in range(N):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])
        for i in range(N):
            if nums[i] > 0:
                res.append(i + 1)
        return res
        # missing_numbers = []
        # i, N = 0, len(arr)
        # while i < N:
        #     j = arr[i] - 1
        #     if arr[i] != arr[j]:
        #         arr[i], arr[j] = arr[j], arr[i]
        #     else:
        #         i += 1
        # for i in range(N):
        #     if arr[i] != i + 1:
        #         missing_numbers.append(i + 1)
        # return missing_numbers