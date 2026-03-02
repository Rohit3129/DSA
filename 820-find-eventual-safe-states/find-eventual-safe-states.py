class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbors in graph[i]:
                if not dfs(neighbors):
                    return False
            safe[i] = True
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
