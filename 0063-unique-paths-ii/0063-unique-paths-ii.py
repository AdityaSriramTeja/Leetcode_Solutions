class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = {}

        def f(row, col): 
            if row == 0 and col == 0 and grid[row][col] == 0: 
                return 1 
            if row < 0 or col < 0 or grid[row][col] : 
                return 0
            if (row,col) in dp: 
                return  dp[(row,col)]
            up = f(row-1, col) 
            left = f(row ,col-1) 
            dp[(row,col)] =  up + left
            return  dp[(row,col)]
        return f(len(grid)-1, len(grid[0])-1)
            