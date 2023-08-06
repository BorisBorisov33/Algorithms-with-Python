def find_all_paths(row, col, labyrinth, direction, path, array_of_paths):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return
    if labyrinth[row][col] == '#':
        return
    if labyrinth[row][col] == 'v':
        return
    path.append(direction)

    if labyrinth[row][col] == 'E':
        result = ''.join(path)
        if result not in array_of_paths:
            array_of_paths[result] = len(result)

    else:
        labyrinth[row][col] = 'v'
        find_all_paths(row, col + 1, labyrinth, 'R', path, array_of_paths)
        find_all_paths(row, col - 1, labyrinth, 'L', path, array_of_paths)
        find_all_paths(row + 1, col, labyrinth, 'D', path, array_of_paths)
        find_all_paths(row - 1, col, labyrinth, 'U', path, array_of_paths)

        labyrinth[row][col] = '.'
    path.pop()


size_of_maze = int(input())

array_of_labirint = []
array_of_paths = {}
for _ in range(size_of_maze):
    array_of_labirint.append(list(input()))

find_all_paths(0, 0, array_of_labirint, '', [], array_of_paths)

smallest_value = min(array_of_paths.values())
print(smallest_value)
