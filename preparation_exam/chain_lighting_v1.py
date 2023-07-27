class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


graph = []

number_of_neighbourhoods = int(input())
number_of_distances = int(input())
number_of_l = int(input())

damage_dictionary = {}
max_node = float('-inf')
for _ in range(number_of_distances):
    from_neigh, to_neigh, distance = [int(x) for x in input().split(" ")]
    graph.append(Edge(from_neigh, to_neigh, distance))
    max_node = max(from_neigh, to_neigh, max_node)
for _ in range(number_of_l):
    neighbourhood, damage = [int(x) for x in input().split(" ")]
    if neighbourhood not in damage_dictionary:
        damage_dictionary[neighbourhood] = []
    if damage not in damage_dictionary[neighbourhood]:
        damage_dictionary[neighbourhood] = damage

parent = [num for num in range(max_node + 1)]

forest = []
damage_list = [0] * number_of_neighbourhoods
for neigh, damage_in_dictionary in damage_dictionary.items():
    damage_list[neigh] = damage_in_dictionary
    for edge in sorted(graph, key=lambda e: e.weight):
        first_node_root = find_root(parent, edge.first)
        second_node_root = find_root(parent, edge.second)
        if first_node_root != second_node_root:
            parent[first_node_root] = second_node_root
            if damage_list[first_node_root] == 0 and damage_list[second_node_root] != 0:
                damage_list[first_node_root] += damage_list[second_node_root] // 2
            if damage_list[second_node_root] == 0 and damage_list[first_node_root] != 0:
                damage_list[second_node_root] += damage_list[first_node_root] // 2
            forest.append(edge)

print(damage_list)
for edge in forest:
    print(f'{edge.first} - {edge.second}')
