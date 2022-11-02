class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        def distance(elem: int) -> int:
            nonlocal x
            return abs(elem - x)

        max_heap = []
        for i in range(k):
            heappush(max_heap, (-distance(nums[i]), nums[i]))

        for i in range(k, len(nums)):
            num_dist = distance(nums[i])
            if num_dist < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-distance(nums[i]), nums[i]))

        res = []
        for dist, num in max_heap:
            res.append(num)
        res.sort()
        return res