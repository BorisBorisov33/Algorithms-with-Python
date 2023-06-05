nums = [1, 2, 3, 5, 4, 6]

target = 5


def linear_search(nums, target):
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1


print(linear_search(nums, target))
