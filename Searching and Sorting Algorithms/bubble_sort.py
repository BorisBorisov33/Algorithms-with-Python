nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted=True
    for index in range(1, len(nums) - counter):
        if nums[index] < nums[index - 1]:
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
            is_sorted=False
    counter += 1

print(*nums, sep=' ')