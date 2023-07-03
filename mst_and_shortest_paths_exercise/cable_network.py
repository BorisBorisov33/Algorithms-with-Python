from queue import PriorityQueue
# use prim algorithm
class Edge:
    def __init__(self, first, second, weight):
        self.start = first
        self.end = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
tree = set()

for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(second, first, weight))
    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)


pq = PriorityQueue()
for node in tree:
    for edge in graph[node]:
        pq.put(edge)


budget_used = 0
while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.start in tree and min_edge.end not in tree:
        non_tree_node = min_edge.end
    elif min_edge.start not in tree and min_edge.end in tree:
        non_tree_node = min_edge.start

    if non_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break

    budget_used+=min_edge.weight

    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')