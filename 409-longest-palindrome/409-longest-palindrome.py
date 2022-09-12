from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        num_pairs = 0
        for count in counter.values():
            if count > 1:
                num_pairs += count // 2
        if num_pairs * 2 < len(s): return num_pairs * 2 + 1
        return num_pairs * 2