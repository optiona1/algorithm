def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = base

