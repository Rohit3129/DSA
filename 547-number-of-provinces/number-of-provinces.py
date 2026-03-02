class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces += 1
                stack = [i]
                visited[i] = True
                while stack:
                    node = stack.pop()
                    for j in range(n):
                        if isConnected[node][j] and not visited[j]:
                            visited[j] = True
                            stack.append(j)
        return provinces