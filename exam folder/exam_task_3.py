def find_best_longest_increasing_sequence(goals):
    n = len(goals)
    size = [1] * n
    parent_array = [None] * n
    best_index = 0

    for current in range(1, n):
        for previous in range(current - 1, -1, -1):
            if goals[previous] <= goals[current]:
                if size[previous] + 1 >= size[current]:
                    size[current] = size[previous] + 1
                    parent_array[current] = previous

        if size[current] > size[best_index]:
            best_index = current

    result = []
    while best_index is not None:
        result.append(goals[best_index])
        best_index = parent_array[best_index]

    return reversed(result)


if __name__ == '__main__':
    goals = list(map(int, input().split(', ')))
    best_increasing_sequence = find_best_longest_increasing_sequence(goals)
    print(*best_increasing_sequence)
