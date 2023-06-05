nums = [int(x) for x in input().split()]
# target = int(input())

for idx in range(len(nums)):
    current_number = int(nums[idx])

    min_num = current_number
    min_idx = idx
    for next_index in range(idx + 1, len(nums)):
        next_number = nums[next_index]
        if next_number < min_num:
            min_num = next_number
            min_idx = next_index
            nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums, sep=' ')
