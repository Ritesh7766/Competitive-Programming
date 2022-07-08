class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        weight = {}
        
        for i, equation in enumerate(equations):
            x, y = equation
            graph[x].append(y)
            graph[y].append(x)
            weight[(x, y)] = values[i]
            weight[(y, x)] = 1 / values[i]
        
        def bfs(start, end):
            if start not in graph.keys(): return -1
            queue = collections.deque()
            queue.append((start, 1))
            visited = set([start])
            
            while queue:
                u, val = queue.popleft()
                if u == end: return val
                for v in graph[u]:
                    if v in visited: continue
                    visited.add(v)
                    queue.append((v, weight[(u, v)] * val))
            return -1
        
        res = []
        for x, y in queries:
            res.append(bfs(x, y))
        return res