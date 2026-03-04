class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph:
            return 0
        n = len(graph)
        target = (1 << n) - 1
        queue = deque()
        visited = [[False] * (1<<n) for _ in range(n)]
        for i in range(n):
            mask  = 1 << i
            queue.append((i, mask))
            visited[i][mask] = True
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node, mask = queue.popleft()
                if mask == target:
                    return steps
                for neigh in graph[node]:
                    new_mask = mask | (1 << neigh)
                     
                    if not visited[neigh][new_mask]:
                        visited[neigh][new_mask] = True
                        queue.append((neigh, new_mask))
            steps += 1
        return -1