class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_cells = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_cells.append((i,j))
        for cell in zero_cells:
            for x in range(n):
                matrix[cell[0]][x] = 0
            for y in range(m):
                matrix[y][cell[1]] = 0
        

        