class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        class SlidingWindowMedian:
            def __init__(self):
                self.maxHeap, self.minHeap = [], []

            def find_sliding_window_median(self, nums, k):
                result = [0.0 for x in range(len(nums) - k + 1)]
                for i in range(0, len(nums)):
                    self.insert(nums[i])

                    if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
                        result[i - k + 1] = self.find_median()
                        self.remove_element(nums[i - k + 1])

                return result

            def insert(self, num):
                if not self.maxHeap or num <= -self.maxHeap[0]:
                    heappush(self.maxHeap, -num)
                else:
                    heappush(self.minHeap, num)

                self.rebalance_heaps()

            # removes an element from the heap keeping the heap property
            def remove(self, heap, element):
                ind = heap.index(element)  # find the element
                # move the element to the end and delete it
                heap[ind] = heap[-1]
                del heap[-1]
                # we can use heapify to readjust the elements but that would be O(N),
                # instead, we will adjust only one element which will O(logN)
                if ind < len(heap):
                    heapq._siftup(heap, ind)
                    heapq._siftdown(heap, 0, ind)

            def remove_element(self, element_to_remove):
                if element_to_remove <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -element_to_remove)
                else:
                    self.remove(self.minHeap, element_to_remove)

                self.rebalance_heaps()

            def rebalance_heaps(self):
                # either both the heaps will have equal number of elements or max-heap will have
                # one more element than the min-heap
                if len(self.maxHeap) > len(self.minHeap) + 1:
                    heappush(self.minHeap, -heappop(self.maxHeap))
                elif len(self.maxHeap) < len(self.minHeap):
                    heappush(self.maxHeap, -heappop(self.minHeap))

            def find_median(self) -> int:
                if len(self.maxHeap) == len(self.minHeap):
                    return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else:  # because max-heap will have one more element than the min-heap
                    return -self.maxHeap[0] / 1.


        result = SlidingWindowMedian()
        return result.find_sliding_window_median(nums, k)