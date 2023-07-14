def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(dep):
    for node, dependencies in dep.items():
        if dependencies == 0:
            return node
    return None


nodes = int(input())
edges = int(input())

graph = {}

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

has_cycles = False
sorted_nodes = []

dep = find_dependencies(graph)
while dep:
    node_to_remove = find_node_without_dependencies(dep)
    # print(node_to_remove)

    if node_to_remove is None:
        has_cycles = True
        break

    sorted_nodes.append(node_to_remove)
    dep.pop(node_to_remove)

    for child in graph[node_to_remove]:
        dep[child] -= 1

print(sorted_nodes)