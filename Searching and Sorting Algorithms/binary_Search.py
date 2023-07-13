def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_el = nums[mid]

        if mid_el == target:
            return mid

        if target > mid_el:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
