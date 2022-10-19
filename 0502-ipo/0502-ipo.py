from heapq import *
class Solution:
    def findMaximizedCapital(self, projects: int, curr_capital: int, profits: List[int], capitals: List[int]) -> int:
        min_capital_heap = []
        max_profit_heap = []

        for i, capital in enumerate(capitals):
            heappush(min_capital_heap, [capital, i])

        for _ in range(projects):
            while min_capital_heap and min_capital_heap[0][0] <= curr_capital:
                profit_idx = heappop(min_capital_heap)[1]
                heappush(max_profit_heap, -profits[profit_idx])

            if not max_profit_heap:
                break
            curr_capital += -heappop(max_profit_heap)

        return curr_capital