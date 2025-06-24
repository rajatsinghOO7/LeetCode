from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)

        visited = [0] * n
        count = 0

        def dfs(node):
            visited[node] = 1
            for neighbour in adjList[node]:
                if visited[neighbour] == 0:
                    dfs(neighbour)

        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i)

        return count
