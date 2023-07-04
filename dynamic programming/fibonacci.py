def calc_fibb(n, memo):
    # we look for the key in the dictionary
    if n in memo:
        # we return the value of the key in the dictionary
        return memo[n]

    if n <= 2:
        return 1
    result = calc_fibb(n - 1, memo) + calc_fibb(n - 2, memo)
    # assign the value(result) in the dictionary under the given key (n)
    memo[n] = result
    return result


number = int(input())
print(calc_fibb(number, {}))
