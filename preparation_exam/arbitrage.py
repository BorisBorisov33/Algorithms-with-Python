from collections import deque
from queue import PriorityQueue

number_of_pairs = int(input())

graph = []
[graph.append([]) for _ in range(number_of_pairs)]

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

    graph[from_curr].append((from_curr, to_curr, price))
    graph[to_curr].append((from_curr, to_curr, price))

start_node = input()
if start_node == 'GBP':
    start_node = 1
elif start_node == 'USD':
    start_node = 2
elif start_node == 'AUD':
    start_node = 3
elif start_node == 'NZD':
    start_node = 4

# next_node = start_node + 1

pq = PriorityQueue()
pq.put((1, start_node))

prices = [float('-inf')] * number_of_pairs
prices[start_node] = -1
parent = [None] * number_of_pairs
total = 0

while not pq.empty():
    max_price, node = pq.get()
    for from_node, to_node, coefficient in graph[node]:
            new_price = max_price * coefficient
            if new_price > prices[to_node]:
                prices[to_node] = new_price
                parent[to_node] = node
                pq.put((new_price, to_node))

print(total)

# print the path backward by getting the parent of the node
path = deque()
node = 4
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep=' -> ')
