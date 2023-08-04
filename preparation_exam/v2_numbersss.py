def find_ways(number, current_sum, path, last_number):
    if current_sum == number:
        print(" + ".join(str(x) for x in path))
        return

    for i in range(min(number - current_sum, last_number), 0, -1):
        find_ways(number, current_sum + i, path + [i], i)


if __name__ == "__main__":

    number = int(input())
    if 0 <= number <= 100:
        find_ways(number, 0, [], number)
