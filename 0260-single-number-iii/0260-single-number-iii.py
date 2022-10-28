class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        right_most_set = 1
        while xor_sum & right_most_set == 0:
            right_most_set <<= 1

        num_1, num_2 = 0, 0
        for num in nums:
            if num & right_most_set != 0:
                num_1 ^= num
            else:
                num_2 ^= num

        return [num_1, num_2]