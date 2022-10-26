class Solution:
    def search(self, nums: List[int], key: int) -> int:
        start, end = 0, len(nums) - 1
        is_ascending = nums[start] < nums[end]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == key:
                return mid
            else:
                if is_ascending:
                    if key > nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if key < nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1
            