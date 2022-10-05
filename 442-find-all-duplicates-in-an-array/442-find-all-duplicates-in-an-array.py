class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i, N = 0, len(arr)
        while i < N:
            j = arr[i] - 1
            if arr[j] != arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1

        duplicates = []
        for i in range(N):
            if arr[i] != i + 1:
                duplicates.append(arr[i])
        return duplicates