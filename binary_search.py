def binary_search(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return -1


def binary_search_lcro(nums: list[int], target: int) -> int:
    i, j = 0, len(nums)
    while i < j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m
        else:
            return m

    return -1


def test_binary_search():
    # 测试用例
    test_cases = [
        {"nums": [1, 2, 3, 4, 5], "target": 3, "expected": 2},
        {"nums": [1, 2, 3, 4, 5], "target": 6, "expected": -1},
        {"nums": [1, 2, 3, 4, 5], "target": 1, "expected": 0},
        {"nums": [1, 2, 3, 4, 5], "target": 5, "expected": 4},
        {"nums": [1, 2, 3, 4, 5], "target": 0, "expected": -1},
        {"nums": [], "target": 1, "expected": -1},
        {"nums": [1], "target": 1, "expected": 0},
        {"nums": [1], "target": 2, "expected": -1},
        {"nums": [1, 2], "target": 1, "expected": 0},
        {"nums": [1, 2], "target": 2, "expected": 1},
        {"nums": [1, 2], "target": 3, "expected": -1},
    ]

    # 测试 binary_search 函数
    print("测试 binary_search 函数：")
    for case in test_cases:
        result = binary_search(case["nums"], case["target"])
        assert result == case["expected"], f"binary_search({case['nums']}, {case['target']}) = {result}, 预期 {case['expected']}"
        print(f"binary_search({case['nums']}, {case['target']}) = {result}, 预期 {case['expected']}")

    # 测试 binary_search_lcro 函数
    print("\n测试 binary_search_lcro 函数：")
    for case in test_cases:
        result = binary_search_lcro(case["nums"], case["target"])
        assert result == case["expected"], f"binary_search_lcro({case['nums']}, {case['target']}) = {result}, 预期 {case['expected']}"
        print(f"binary_search_lcro({case['nums']}, {case['target']}) = {result}, 预期 {case['expected']}")

# 调用测试函数
if __name__ == '__main__':
    test_binary_search()
