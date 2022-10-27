class Solution:
    def nextGreatestLetter(self, arr: List[str], key: str) -> str:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2

            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return arr[start % len(arr)]