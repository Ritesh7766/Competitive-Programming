class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        color, all_colors = {}, set([1, 2, 3, 4])
        
        
        for node in range(1, n + 1):
            taken = set()
            for adj_v in graph[node]:
                if adj_v in color:
                    taken.add(color[adj_v])
            for col in all_colors - taken:
                color[node] = col
                break
        return color.values()