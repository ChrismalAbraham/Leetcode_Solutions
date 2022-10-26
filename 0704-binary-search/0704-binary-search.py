class Solution:
    def search(self, nums: List[int], key: int) -> int:
        if not nums:
            return -1
        descending = False
        if len(nums) > 1 and nums[-1] < nums[1]:
            descending = True
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == key:
                return mid
            else:
                if not descending:
                    if key > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if key < nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1
        
        
        
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return mid
        # return -1
            