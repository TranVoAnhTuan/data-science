class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i in range(len(edges)):
            u,v = edges[i]
            w = succProb[i]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        queue = [(start, -1.0)]
        visited = {start: -1.0}
        while queue:
            node, probability = heappop(queue)
            if node == end:
                return -probability
            for neigh, weight in graph.get(node, []):
                newProbability = probability * weight
                if newProbability > visited.get(neigh, 0.0):
                    continue
                visited[neigh] = newProbability
                heappush(queue, (neigh, newProbability))
        return 0.0
