def digit(num: int, exp: int) -> int:
    return (num // exp) % 10


def counting_sort_digit(nums: list[int], exp: int):
    counter = [0] * 10
    n = len(nums)
    for i in range(n):
        d = digit(nums[i], exp)
        counter[d] += 1

    for i in range(1, 10):
        counter[i] += counter[i - 1]

    res = [0] * n
    for i in range(n-1, -1, -1):
        d = digit(nums[i], exp)
        j = counter[d] - 1
        res[j] = nums[i]
        counter[d] -= 1

    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums: list[int]):
    m = max(nums)
    exp = 1
    while exp <= m:
        counting_sort_digit(nums, exp)
        exp *= 10


if __name__ == '__main__':
    lst = [3, 1, 2, 6, 9, 7, 2, 1]
    radix_sort(lst)
    print(lst)
