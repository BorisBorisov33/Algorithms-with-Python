from collections import deque

nodes = int(input())
edges = int(input())

graph = {}
visited = set()
cycles = set()

sorted_nodes = deque()


def top_sort(node, sorted_nodes, graph, visited, cycles):
    if node in visited:
        return
    visited.add(node)
    for child in graph:
        top_sort(child, sorted_nodes, graph, visited, cycles)
    sorted_nodes.appendleft(node)

    return sorted_nodes


for node in graph:
    top_sort(node, sorted_nodes, graph, visited)
for _ in range(edges):
    source, destination = input().split()
    source = int(source)
    destination = int(destination)

    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

start_node = int(input())

print(top_sort(1, sorted_nodes, graph, visited, cycles))
w