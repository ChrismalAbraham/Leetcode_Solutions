class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        class Point:
            def __init__(self, arr):
                self.x = arr[0]
                self.y = arr[1]

            def distance_from_origin(self):
                return self.x ** 2 + self.y ** 2

            def __lt__(self, other):  # less than overrule
                # self is probably the lower node and other is probably the root/upper node
                return self.distance_from_origin() > other.distance_from_origin()
            
            def coordinates(self):
                return [self.x, self.y]


        max_heap = []
        for i in range(k):
            heappush(max_heap, Point(points[i]))
        for i in range(k, len(points)):
            curr_point = Point(points[i])
            if curr_point.distance_from_origin() < max_heap[0].distance_from_origin():
                heappop(max_heap)
                heappush(max_heap, curr_point)
        res = []
        for point in max_heap:
            res.append(point.coordinates())
        return res