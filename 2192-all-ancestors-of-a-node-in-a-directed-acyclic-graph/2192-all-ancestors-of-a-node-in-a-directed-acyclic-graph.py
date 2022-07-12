class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        res = [set() for _ in range(n)]
        visited = set()
        
        def dfs(u):
            if u in visited:
                return res[u]
            visited.add(u)
            for v in graph[u]:
                res[u].add(v)
                res[u] = res[u] | dfs(v)
            return res[u]
        
        for u in range(n):
            if u in visited: continue
            _ = dfs(u)
        return [sorted(r) for r in res]