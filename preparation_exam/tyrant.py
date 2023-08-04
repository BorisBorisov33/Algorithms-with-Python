def minSum(arr, num):
    dp = [0] * num

    if num == 1:
        return arr[0]
    if num == 2:
        return min(arr[0], arr[1])

    if num == 3:
        return min(arr[0], min(arr[1], arr[2]))

    if num == 4:
        return min(min(arr[0], arr[1]), min(arr[2], arr[3]))

    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[2]
    dp[3] = arr[3]

    for i in range(4, num):
        dp[i] = arr[i] + min(min(dp[i - 1], dp[i - 2]),
                             min(dp[i - 3], dp[i - 4]))
    return min(min(dp[num - 1], dp[num - 2]),
               min(dp[num - 3], dp[num - 4]))


array = [int(x) for x in input().split()]
num = len(array)
print(minSum(array, num))
