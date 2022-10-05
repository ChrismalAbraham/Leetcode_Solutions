class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        i, N = 0, len(arr)
        while i < N:
            j = arr[i] - 1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                if i != j:
                    return arr[i]
                i += 1