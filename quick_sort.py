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
    sorted_arr = quick_sort(example_arr)
    print("排序后:", sorted_arr)
