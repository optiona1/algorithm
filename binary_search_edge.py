from binary_search_insertion import binary_search_insertion, binary_search_insertion_right


def binary_search_left_edge(nums: list[int], target: int) -> int:
    i = binary_search_insertion(nums, target)

    if i == len(nums) or nums[i] != target:
        return -1

    return i


def binary_search_right_edge1(nums: list[int], target: int) -> int:
    i = binary_search_insertion_right(nums, target)

    if i == len(nums) or nums[i] != target:
        return -1

    return i

def binary_search_right_edge2(nums: list[int], target: int) -> int:
    i = binary_search_insertion(nums, target + 1)
    j = i - 1

    if j == -1 or nums[j] != target:
        return -1

    return j

