class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        merged_intervals = []
        start, end, i = 0, 1, 0
        N = len(intervals)
        # while the new intervals start is greater than the first couple intervals ends
        while i < N and intervals[i][end] < new_interval[start]:
            merged_intervals.append(intervals[i])
            i += 1
        # while the start of the current overlaps with the end of the new_interval change the start and end values to be appended
        while i < N and intervals[i][start] <= new_interval[end]:
            new_interval[start] = min(new_interval[start], intervals[i][start])
            new_interval[end] = max(new_interval[end], intervals[i][end])
            i += 1
        merged_intervals.append(new_interval)
        # insert the rest of the intervals into the new array
        while i < N:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals