class Solution:
    def findClosestElements(self, nums: List[int], nums_of_elem: int, target: int) -> List[int]:
        def binary_search(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    return mid
            return end if end > -1 else 0 # if num does not exist in array then end will always points to the number directly less than target

        def dist(num):
            nonlocal target
            return abs(num - target)

        closest_idx = binary_search(nums, target)

        left, right = closest_idx, closest_idx + 1
        queue = deque()

        while len(queue) < nums_of_elem:
            if left < 0: # first 2 if conditions are out of bounds checks
                queue.append(nums[right])
                right += 1
            elif right >= len(nums):
                queue.appendleft(nums[left])
                left -= 1
            elif dist(nums[left]) <= dist(nums[right]): # if distance is equal append left
                queue.appendleft(nums[left])
                left -= 1
            else:
                queue.append(nums[right])
                right += 1

        return queue

#         def binary_search(nums, target):
#             start, end = 0, len(nums) - 1
#             while start <= end:
#                 mid = start + (end - start) // 2
#                 if target < nums[mid]:
#                     end = mid - 1
#                 elif target > nums[mid]:
#                     start = mid + 1
#                 else:
#                     return mid
#             return mid

#         closest_index_to_k = binary_search(nums, target)
#         high, low = closest_index_to_k + num_of_elem, closest_index_to_k - num_of_elem
#         # don't want the ends of our ranges to be outside the array bounds when indexing
#         high, low = min(high, len(nums) - 1), max(low, 0)

#         min_heap = []
#         for i in range(low, high + 1):
#             heappush(min_heap, (abs(nums[i] - target), nums[i]))

#         res = []
#         for i in range(num_of_elem):
#             res.append(heappop(min_heap)[1])
#         res.sort()
#         return res