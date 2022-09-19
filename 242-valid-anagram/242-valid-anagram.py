class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_s = [0] * 26
        letter_count_t = [0] * 26
        for char in s:
            letter_count_s[ord(char) - ord('a')] += 1
        for char in t:
            letter_count_t[ord(char) - ord('a')] += 1
        return letter_count_s == letter_count_t
    
    # can also use
    # return colletions.Counter(s) == collections.Counter(t)
            