class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Given an integer rowIndex, return the rowIndexth (0-indexed)
        row of the Pascal's triangle.
        """
        triangle = [[1] * i for i in range(1, rowIndex + 2)]

        for row in range(2, len(triangle)):
            for col in range(1, len(triangle[row]) - 1):
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        return triangle[rowIndex]
        