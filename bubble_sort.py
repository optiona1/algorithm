def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def bubble_sort_with_flag(nums: list[int]):
    n = len(nums)
    for i in range(n-1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break

