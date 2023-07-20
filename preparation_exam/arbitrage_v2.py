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

end_node = 0
start = input()
if start == 'GBP':
    start = 1
    end_node = 5
elif start == 'USD':
    start = 2
    end_node = 6
elif start == 'AUD':
    start = 3
    end_node = 7
elif start == 'NZD':
    start = 4
    end_node = 8

distance = [float('-inf')] * (number_of_pairs + 1)
distance[start] = 1

parent = [None] * (number_of_pairs + 1)

for node in range(number_of_pairs - 1):
    updated = False
    for from_node, to_node, coefficient in graph[node]:
        if distance[from_node] == float('-inf'):
            continue
        new_distance = distance[from_node] + coefficient
        if new_distance > distance[to_node]:
            distance[to_node] = new_distance
            parent[to_node] = from_node
            updated = True
    if not updated:
        break

print(parent)
print(distance)