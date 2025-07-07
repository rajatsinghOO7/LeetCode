from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        start_color = image[sr][sc]

        # If the new color is the same as the original, no need to do anything
        if start_color == color:
            return image

        que = deque()
        que.append((sr, sc))
        image[sr][sc] = color  # Color the starting pixel

        dRow = [1, 0, -1, 0]
        dCol = [0, 1, 0, -1]

        while que:
            row, col = que.popleft()
            for i in range(4):
                nextRow = row + dRow[i]
                nextCol = col + dCol[i]
                
                if (0 <= nextRow < n and 0 <= nextCol < m and image[nextRow][nextCol] == start_color):
                    image[nextRow][nextCol] = color
                    que.append((nextRow, nextCol))

        return image
