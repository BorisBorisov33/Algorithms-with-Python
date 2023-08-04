from collections import deque

number_of_gateways = int(input())
num_connections = int(input())
graph = []
[graph.append([]) for _ in range(number_of_gateways + 1)]

for _ in range(num_connections):
    from_node, to_node = [int(x) for x in input().split()]
    graph[from_node].append(to_node)

start_node = int(input())
destination_node = int(input())

visited = [False] * (number_of_gateways + 1)
parent = [None] * (number_of_gateways + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = destination_node
while node is not None:
    path.appendleft(node)
    node = parent[node]
if len(path) != 1:
    print(*path, sep=' ')
else:
    print()
