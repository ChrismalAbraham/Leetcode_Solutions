class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_nums_ex = 0
        for i in range(n + 1):
            xor_nums_ex ^= i
        xor_nums = 0
        for num in nums:
            xor_nums ^= num
        return xor_nums ^ xor_nums_ex