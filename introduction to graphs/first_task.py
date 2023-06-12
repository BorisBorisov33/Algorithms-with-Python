nodes = int(input())

graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes


def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


for node in range(nodes):
    component = []
    dfs(node, graph, visited, component)
    print(component)
