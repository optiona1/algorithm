def counting_sort_naive(nums: list[int]):
    m = max(nums)
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1

    i = 0
    for num in range(m + 1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1


def counting_sort(nums: list[int]):
    m = max(nums)
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1

    for i in range(m):
        counter[i+1] += counter[i]

    n = len(nums)
    res = [0] * n
    for i in range(n - 1, -1, -1):
        num = nums[i]
        res[cuonter[num] - 1] = num
        counter[num] -= 1

    for i in range(n):
        nums[i] = res[i]
