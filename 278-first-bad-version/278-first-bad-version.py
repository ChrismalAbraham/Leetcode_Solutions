# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            test = (start + end) // 2
            if isBadVersion(test): 
                end = test
            else:
                start = test + 1
        return start