from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        # Visited matrix and distance matrix
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        
        # Initialize queue with all 0s
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = 1
        
        # Direction vectors for 4 directions
        del_row = [-1, 0, 1, 0]
        del_col = [0, 1, 0, -1]
        
        while q:
            row, col, steps = q.popleft()
            dist[row][col] = steps
            
            for i in range(4):
                nrow = row + del_row[i]
                ncol = col + del_col[i]
                
                if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol, steps + 1))
        
        return dist
