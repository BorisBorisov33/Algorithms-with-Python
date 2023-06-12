graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: []
}


def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


visited = set()
for node in graph:
    dfs(node, graph, visited)
