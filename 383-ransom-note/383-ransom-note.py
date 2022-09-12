from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ref = Counter(magazine)
        test = Counter(ransomNote)
        for char, count in test.items():
            if count <= ref[char]:
                continue
            else:
                return False
        return True
        