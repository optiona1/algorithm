import time


def median_three(nums: list[int], left:int, mid: int, right: int) -> int:
    l, m, r = nums[left], nums[mid], nums[right]
    if (l <= m <= r) or (r <= m <= l):
        return mid
    if (m <= l <= r) or (r <= l <= m):
        return left
    return right


def partition(nums: list[int], left: int, right: int) -> int:
    med = median_three(nums, left, (left+right) // 2, right)
    nums[left], nums[med] = nums[med], nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort_fast(nums: list[int], left: int, right: int):
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quick_sort_fast(nums, left, pivot - 1)
    quick_sort_fast(nums, pivot + 1, right)


def quick_sort_fast(nums: list[int], left: int, right: int):
    while left < right:
        pivot = partition(nums, left, right)
        if pivot - left < right - pivot:
            quick_sort_fast(nums, left, pivot-1)
            left = pivot + 1
        else:
            quick_sort_fast(nums, pivot+1, right)
            right = pivot - 1

                
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 选择中间元素作为基准值
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序并合并
    return quick_sort(left) + middle + quick_sort(right)


# 示例
if __name__ == "__main__":
    example_arr = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", example_arr)
    start = time.time()
    sorted_arr = quick_sort(example_arr)
    print("耗时:", time.time() - start)
    print("排序后:", sorted_arr)

    print("排序前:", example_arr)
    start = time.time()
    quick_sort_fast(example_arr, 0, len(example_arr)-1)
    print("耗时:", time.time() - start)
    print("排序后:", example_arr)
