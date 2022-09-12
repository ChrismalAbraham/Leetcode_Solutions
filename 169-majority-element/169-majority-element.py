class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            if counter == 0:
                curr = nums[i]
                counter += 1
            elif nums[i] != curr:
                counter -= 1
            else:
                counter += 1
        return curr