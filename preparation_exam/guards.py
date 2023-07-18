from collections import deque
# BFS approach of the task
def countNotReachusingBFS(gr, n):
    visited = [False] * (n + 1)
    pq = deque()
    pq.append(start_node)
    while pq:
        start = pq.popleft()
        visited[start] = True
        for iterable_value in gr[start]:
            if visited[iterable_value]:
                continue
            else:
                pq.append(iterable_value)

    result_array = []
    for i in range(n + 1):
        if i == start_node:
            visited[i] = True
        if i == 0:
            continue

        if not visited[i]:
            result_array.append(i)
    print(*result_array)


graph = {}
nodes = int(input())
edges = int(input())
for _ in range(edges):

    source, destination = [int(x) for x in input().split()]

    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

start_node = int(input())

countNotReachusingBFS(graph, nodes)
