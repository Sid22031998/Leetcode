class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        maxi=0
        for i in range(n-2):
            for j in range(1, m-1):
                maxi=max(maxi, grid[i][j-1]+grid[i][j]+grid[i][j+1]+grid[i+1][j]+grid[i+2][j-1]+grid[i+2][j]+grid[i+2][j+1])
        return maxi
