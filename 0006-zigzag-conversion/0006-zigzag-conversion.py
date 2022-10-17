class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        top, start, bottom = 0, 0, numRows - 1
        # (numRows - 1) * 2
        N = len(s)
        res = []
        while top < N:
            res.append(s[top])
            top += (numRows - 1) * 2
        for _ in range(numRows - 2):
            start += 1
            increment = ((numRows - 1) * 2) - (start * 2)
            reverse_increment = start * 2
            i = start
            flip = True
            while i < N:
                add = increment if flip else reverse_increment
                res.append(s[i])
                i += add
                flip = not flip
        while bottom < N:
            res.append(s[bottom])
            bottom += (numRows - 1) * 2
        
        return "".join(res)