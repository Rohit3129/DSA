class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0 , 0)]
        seen = set()
        seen.add((0, 0))
        max_elev = 0
        while pq:
            elev, r, c = heapq.heappop(pq)
            max_elev = max(max_elev, elev)
            if r == (n - 1) and c == (n-1):
                return max_elev
            for nr, nc in [(r + 1, c), (r, c + 1), (r -1 , c), (r, c - 1)]:
                if nr < 0 or nc < 0  or nr >= n or nc >= n:
                    continue
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                heapq.heappush(pq,(grid[nr][nc], nr, nc))
        return max_elev