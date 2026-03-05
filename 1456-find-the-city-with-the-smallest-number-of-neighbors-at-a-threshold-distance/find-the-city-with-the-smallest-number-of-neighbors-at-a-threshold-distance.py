class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        result_city = -1
        min_reach = float('inf')
        for src in range(n):
            dist = [float('inf')]*n
            dist[src] = 0
            for _ in range(n -1): 
                for u, v, w in edges:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                    if dist[v] + w < dist[u]:
                        dist[u] = dist[v] + w
            count = 0
            for i in range(n):
                if i != src and dist[i] <= distanceThreshold:
                    count += 1
            if count <= min_reach:
                min_reach = count
                result_city = src
        return result_city


