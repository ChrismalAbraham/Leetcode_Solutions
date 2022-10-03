class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_row = False
        # iterates through array to set top row and leftmost column to store which row and column
        # should be set to zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero_row = True
                    matrix[0][c] = 0
        # sets the inner values of the matrix to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # sets the left most column to zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        # sets the top row to zero    
        if zero_row:
            for c in range(COLS):
                matrix[0][c] = 0
                
        
                
                        
                    
        