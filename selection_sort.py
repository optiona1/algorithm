def selection_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
