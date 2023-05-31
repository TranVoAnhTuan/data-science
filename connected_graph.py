def count_connected_graphs(graph):
    visited = set()
    count = 0
    subgraphs = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if (i, j) not in visited and graph[i][j] == 1:
                subgraph = set()
                dfs(graph, (i, j), visited, subgraph)
                subgraphs.append(subgraph)
                count += 1
    return subgraphs, count

def dfs(graph, start, visited, subgraph):
    visited.add(start)
    subgraph.add(start)
    for neighbor in get_neighbors(graph, start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, subgraph)

def get_neighbors(graph, vertex):
    row, col = vertex
    neighbors = []
    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    for i in range(4):
        row1 = row + dx[i]
        col1 = col + dy[i]
        if row1 >= 0 and row1 < len(graph) and col1 >= 0 and col1 < len(graph[0]) and graph[row1][col1] ==1 :
            neighbors.append((row1,col1))
    return neighbors

graph =[[1,1,1,0,0,0],
        [0,0,1,0,0,0],
        [0,1,1,1,1,0],
        [0,0,0,0,0,1],
        [1,1,0,1,0,1],
        [1,0,1,1,0,1]]

subgraphs,count = count_connected_graphs(graph)
print(count)
for i, subgraph in enumerate(subgraphs):
    print(f"Subgraph {i+1}: {subgraph}")
