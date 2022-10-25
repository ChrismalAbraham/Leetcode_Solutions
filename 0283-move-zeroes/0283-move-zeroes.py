class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero, non_zero = 0, 0
        N = len(nums)
        while non_zero < N:
            while zero < N and nums[zero] != 0:
                zero += 1
            if non_zero < zero: non_zero = zero
                
            while non_zero < N and nums[non_zero] == 0:
                non_zero += 1
            
            if zero < N and non_zero < N:
                temp = nums[non_zero]
                nums[non_zero] = nums[zero]
                nums[zero] = temp
            non_zero += 1
            
        
        