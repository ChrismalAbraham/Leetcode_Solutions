class Solution:
    def intervalIntersection(self, a_arr: List[List[int]], b_arr: List[List[int]]) -> List[List[int]]:
        if not a_arr or not b_arr: return []
        
        intersect_intervals = []
        i, j, start, end = 0, 0, 0, 1

        while i < len(a_arr) and j < len(b_arr):

            a_intersect_b = a_arr[i][start] >= b_arr[j][start] and a_arr[i][start] <= b_arr[j][end]
            b_intersect_a = b_arr[j][start] >= a_arr[i][start] and b_arr[j][start] <= a_arr[i][end]

            if a_intersect_b or b_intersect_a:
                intersect_start = max(a_arr[i][start], b_arr[j][start])
                intersect_end = min(a_arr[i][end], b_arr[j][end])
                intersect_intervals.append([intersect_start, intersect_end])

            if a_arr[i][end] < b_arr[j][end]:
                i += 1
            else:
                j += 1

        return intersect_intervals