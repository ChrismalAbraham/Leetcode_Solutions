import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res = []
        carry = 0
        
        for i in range(max(len(a), len(b))):
            A = int(a[i]) if i < len(a) else 0
            B = int(b[i]) if i < len(b) else 0
            
            total = A + B + carry
            char_to_add = str(total % 2)
            res.append(char_to_add)
            carry = total // 2
        
        if carry:
            res.append("1")
        return "".join(res)[::-1]
                
            