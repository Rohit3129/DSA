class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        time  = 1
        timevis = [0] * len(edges)
        for i, edge in enumerate(edges):
            if timevis[i]:
                continue
            startTime = time
            u = i
            while u != -1 and not timevis[u]:
                timevis[u] = time
                time += 1
                u = edges[u]
            if u != -1 and timevis[u] >= startTime:
                ans = max(ans, time - timevis[u])
        return ans