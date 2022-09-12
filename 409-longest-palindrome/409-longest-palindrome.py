from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s) # counters for the english alphabet are constant space
        num_pairs = 0
        for count in counter.values():
            if count > 1:
                num_pairs += count // 2
        max_length = num_pairs * 2
        if num_pairs * 2 < len(s): max_length += 1
        return max_length