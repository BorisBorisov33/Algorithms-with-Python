nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children


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


dep = find_dependencies(graph)
print(dep)
