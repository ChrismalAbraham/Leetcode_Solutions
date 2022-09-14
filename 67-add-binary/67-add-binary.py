import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def to_int(char) -> int:
            return ord(char) - ord('0')
        
        a, b = a[::-1], b[::-1]
        
        if len(a) < len(b):
            min_s, max_s = a, b
        else:
            min_s, max_s = b, a
        
        res_arr = []
        carry = 0
        
        for i in range(len(min_s)):
            total = to_int(min_s[i]) + to_int(max_s[i]) + carry
            res_arr.append(str(total % 2))
            if total > 1:
                carry = 1
            else: carry = 0
                
        for x in range(len(min_s), len(max_s)):
            total = to_int(max_s[x]) + carry
            res_arr.append(str(total % 2))
            if total > 1:
                carry = 1
            else: carry = 0
        
        if carry == 1:
            res_arr.append("1")
        res = "".join(res_arr)
        return res[::-1]
                
            