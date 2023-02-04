class FloydWarshall:
    def __init__(self, graph):
        self.V = len(graph)
        self.graph = list(map(lambda i : list(map(lambda j : j, i)), graph))
    
    def floydWarshall(self):
        dist = self.graph.copy()
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        self.printSolution(dist)

    def printSolution(self, dist):
        print("Following matrix shows the shortest distances between every pair of vertices:")
        for i in range(self.V):
            for j in range(self.V):
                if(dist[i][j] == INF):
                    print("INF", end="\t")
                else:
                    print(dist[i][j], end="\t")
            print("\n")

INF = 99999
graph = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]
floyd = FloydWarshall(graph)
floyd.floydWarshall()
