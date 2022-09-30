class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(nums, x, y):
            nums[x], nums[y] = nums[y], nums[x]

        low, high = 0, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                swap(nums, i, low)
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, high)
                high -= 1
        