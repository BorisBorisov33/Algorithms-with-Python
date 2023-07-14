def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def find_solution(expression):
    array = (find_indices(expression, '?'))

    for i in reversed(array):
        boolean = expression[i - 1]
        true_result = int(expression[i + 1])
        false_result = int(expression[i + 3])
        if boolean == "t":
            next_true_val = true_result
            if len(expression) == 5:
                print(next_true_val)
                break
            expression[i - 1] = next_true_val
            expression.pop(i)
            expression.pop(i)
            expression.pop(i)
            expression.pop(i)

            continue
        else:
            next_false_val = false_result

            if len(expression) == 5:
                print(next_false_val)
                break

            expression[i - 1] = next_false_val
            expression.pop(i)
            expression.pop(i)
            expression.pop(i)
            expression.pop(i)


line = input().split()
find_solution(line)
