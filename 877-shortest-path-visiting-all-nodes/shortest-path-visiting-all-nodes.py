class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n =  len(graph)
        final_mask = (1 << n) - 1
        heap = []
        dist = {}
        for i in range(n):
            mask = 1 << i
            heapq.heappush(heap, (0,i,mask))
            dist[(i, mask)] = 0
        while heap:
            d, node, mask = heapq.heappop(heap)
            if mask == final_mask:
                return d
            if dist[(node, mask)] < d:
                continue
            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                new_dist = d + 1
                if (nei, new_mask) not in dist or dist[(nei, new_mask)] > new_dist:
                    dist[(nei, new_mask)] = new_dist
                    heapq.heappush(heap, (new_dist, nei, new_mask))
