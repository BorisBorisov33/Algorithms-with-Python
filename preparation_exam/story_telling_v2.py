# source removal or dfs is the solution to go
# I will use topological order with dfs
from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)

    # print(node)
    result.appendleft(node)


result = deque()
graph = {}
while True:
    line = input()
    if line == 'End':
        break
    node, children_str = [x.strip() for x in line.split('->')]
    children = children_str.split()
    graph[node] = children

visited = set()

for node in graph:
    dfs(node, graph, visited, result)

print(*result, sep=' ')
