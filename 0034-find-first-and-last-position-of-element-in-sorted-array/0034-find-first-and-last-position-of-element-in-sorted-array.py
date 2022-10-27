class Solution:
    def searchRange(self, nums: List[int], key: int) -> List[int]:
        def find_range(nums: list, key: int, find_end: bool):
            key_index = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if key < nums[mid]:
                    end = mid - 1
                elif key > nums[mid]:
                    start = mid + 1
                else:  # key == nums[mid]
                    key_index = mid
                    if find_end:
                        start = mid + 1
                    else:
                        end = mid - 1
            return key_index
        res = [-1, -1]
        res[0] = find_range(nums, key, False)
        if res[0] != -1:
            res[1] = find_range(nums, key, True)
        return res