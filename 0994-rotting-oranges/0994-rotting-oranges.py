from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append((i, j, 0))
        
        dRow = [1, 0, -1, 0]
        dCol = [0, 1, 0, -1]
        maxi = 0
        
        while que:
            row, col, time = que.popleft()
            maxi = max(maxi, time)
            
            for i in range(4):
                nextRow = row + dRow[i]
                nextCol = col + dCol[i]
                
                if (0 <= nextRow < n and 0 <= nextCol < m and grid[nextRow][nextCol] == 1):
                    grid[nextRow][nextCol] = 2  # mark as rotten
                    que.append((nextRow, nextCol, time + 1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return maxi
