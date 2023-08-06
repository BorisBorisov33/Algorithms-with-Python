
import heapq
# using heapq
num_roads = int(input())
graph = {}
for _ in range(num_roads):
    source, destination, distance = input().split(' - ')
    distance = int(distance)

    if source not in graph:
        graph[source] = {}
    if destination not in graph:
        graph[destination] = {}
    graph[source][destination] = distance
    graph[destination][source] = distance

closed_roads = set(input().split(","))

start_city = input()
end_city = input()

pq = [(0, start_city)]
distances = {city: float('inf') for city in graph}
distances[start_city] = 0

while pq:
    min_distance, node = heapq.heappop(pq)
    if node == end_city:
        break
    if distances[node] < min_distance:
        continue
    for neighbor, weight in graph[node].items():
        if f'{node}-{neighbor}' in closed_roads or f'{neighbor}-{node}' in closed_roads:
            continue

        new_distance = distances[node] + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heapq.heappush(pq,(new_distance, neighbor))

path = [end_city]
while path[-1] != start_city:
    current_city = path[-1]
    for neighbor, weight in graph[current_city].items():
        if distances[current_city] == distances[neighbor] + weight:
            path.append(neighbor)
            break
path.reverse()

path, total_distance = (' - '.join(path), distances[end_city])
print(path)
print(total_distance)


