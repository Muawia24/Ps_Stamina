class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * i for i in range(1, numRows + 1)]

        for row in range(2, numRows):
            for col in range(1, len(triangle[row]) - 1):
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        return triangle



        