class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def search_pair(nums, target, left, res):
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    res.append([-target, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            search_pair(nums, -nums[i], i + 1, res)
        return res