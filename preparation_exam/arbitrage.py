from collections import deque
from queue import PriorityQueue


class Pair:
    def __init__(self, from_coeff, to_coeff, coeff):
        self.from_coeff = from_coeff
        self.to_coeff = to_coeff
        self.coeff = coeff


number_of_pairs = int(input())

graph = []
[graph.append([]) for _ in range(number_of_pairs)]
# print(graph)

for _ in range(number_of_pairs):
    line = input().split()
    from_curr, to_curr, price = line[0], line[1], float(line[2])

    if from_curr == 'GBP':
        from_curr = 1
    elif from_curr == 'USD':
        from_curr = 2
    elif from_curr == 'AUD':
        from_curr = 3
    elif from_curr == 'NZD':
        from_curr = 4

    if to_curr == 'GBP':
        to_curr = 1
    elif to_curr == 'USD':
        to_curr = 2
    elif to_curr == 'AUD':
        to_curr = 3
    elif to_curr == 'NZD':
        to_curr = 4

    triple = Pair(from_curr, to_curr, price)
    graph[from_curr].append(triple)
    graph[to_curr].append(triple)

start_node = input()
if start_node == 'GBP':
    start_node = 1
elif start_node == 'USD':
    start_node = 2
elif start_node == 'AUD':
    start_node = 3
elif start_node == 'NZD':
    start_node = 4

pq = PriorityQueue()
pq.put((-1, start_node))

prices = [float('-inf')] * number_of_pairs
prices[start_node] = 1
parent = [None] * number_of_pairs

while not pq.empty():
    max_price, node = pq.get()
    # if node == start_node:
    #     break

    for triple in graph[node]:
        child = triple.to_coeff if triple.from_coeff==node else triple.from_coeff
        new_price = -max_price * triple.coeff
        if new_price > prices[child]:
            prices[child] = new_price
            parent[child] = node
            pq.put((-new_price, child))
# change the sign on the upper level
# print(prices[end_node])

# print the path backward by getting the parent of the node
# path = deque()
# # node = end_node
# while node is not None:
#     path.appendleft(node)
#     node = parent[node]
# print(*path, sep=' -> ')
