class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with 1 values
        triangle = [[1] * i for i in range(1, numRows + 1)]

        # Loop throwgh each row starting from triangle[2]
        for row in range(2, numRows):
            #loop throw each column of triangle[row]
            for col in range(1, len(triangle[row]) - 1):
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        return triangle