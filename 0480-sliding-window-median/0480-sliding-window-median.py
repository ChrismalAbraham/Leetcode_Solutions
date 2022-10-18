class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        class SlidingWindowMedian():
            def __init__(self):
                self.min_heap = []
                self.max_heap = []

            def find_sliding_window_median(self, nums: list, k: int) -> list:
                median_list = [0.0 for x in range(len(nums) - k + 1)]
                for i in range(len(nums)):
                    self.insert(nums[i])

                    if i - k + 1 >= 0:  # if there are k elements in the window then calculate median
                        median_list[i - k + 1] = self.find_median()
                        self.remove_element(nums[i - k + 1])

                return median_list

            def insert(self, num):
                if not self.max_heap or num < -self.max_heap[0]:
                    heappush(self.max_heap, -num)
                else:
                    heappush(self.min_heap, num)
                self.rebalance_heaps()

            def remove_element(self, num):
                if num <= -self.max_heap[0]:
                    self.remove(self.max_heap, -num)
                else:
                    self.remove(self.min_heap, num)
                self.rebalance_heaps()

            def remove(self, heap, num):
                idx = heap.index(num)
                heap[idx] = heap[-1]
                del heap[-1]
                if idx < len(heap):
                    heapq._siftup(heap, idx)
                    heapq._siftdown(heap, 0, idx)

            def rebalance_heaps(self):
                if len(self.max_heap) > len(self.min_heap) + 1:
                    heappush(self.min_heap, -heappop(self.max_heap))
                elif len(self.max_heap) < len(self.min_heap):
                    heappush(self.max_heap, -heappop(self.min_heap))

            def find_median(self) -> int:
                if len(self.max_heap) == len(self.min_heap):
                    return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
                else:
                    return -self.max_heap[0] / 1.0

        sliding_window_list = SlidingWindowMedian()
        return sliding_window_list.find_sliding_window_median(nums, k)