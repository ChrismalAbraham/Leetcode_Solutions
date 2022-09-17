class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum, rolling_sum = float(-inf), 0
        for num in nums:
            rolling_sum = max(rolling_sum + num, num)
            maximum_sum = max(maximum_sum, rolling_sum)
        return maximum_sum
