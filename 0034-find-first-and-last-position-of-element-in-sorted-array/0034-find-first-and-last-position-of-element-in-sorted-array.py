class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_range(nums, key, find_end):
            key_index = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if key < nums[mid]:
                    end = mid - 1
                elif key > nums[mid]:
                    start = mid + 1
                else:
                    key_index = mid
                    if find_end:
                        start = mid + 1
                    else:
                        end = mid - 1
            return key_index
        
        result = [-1, -1]
        result[0] = find_range(nums, target, False)
        if result[0] != -1:
            result[1] = find_range(nums, target, True)
        return result