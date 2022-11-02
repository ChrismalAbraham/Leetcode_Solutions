class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        def binary_search(nums, x):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if x < nums[mid]:
                    end = mid - 1
                elif x > nums[mid]:
                    start = mid + 1
                else:
                    return mid
            return mid

        closest_index_to_k = binary_search(nums, x)
        high, low = closest_index_to_k + k, closest_index_to_k - k
        # don't want the ends of our ranges to be outside the array bounds when indexing
        high, low = min(high, len(nums) - 1), max(low, 0)

        min_heap = []
        for i in range(low, high + 1):
            heappush(min_heap, (abs(nums[i] - x), nums[i]))
        
        res = []
        for i in range(k):
            res.append(heappop(min_heap)[1])
        res.sort()
        return res