def sift_down(nums: list[int], n: int, i: int):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        ma = i
        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r

        if ma == i:
            break
        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma


def heap_sort(nums: list[int]):
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)
    for i in range(len(nums)-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
