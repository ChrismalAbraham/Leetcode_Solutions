class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(points: List[int]) -> int:
            return points[0] ** 2 + points[1] ** 2
        max_heap = []
        for i in range(k):
            heappush(max_heap, (-calc_distance(points[i]), points[i][0], points[i][1]))
        for i in range(k, len(points)):
            if calc_distance(points[i]) < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-calc_distance(points[i]), points[i][0], points[i][1]))
        return [[x, y] for d, x, y in max_heap]