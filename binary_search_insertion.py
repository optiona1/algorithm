def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            return m
    return i


def binary_search_insertion(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1

    return i

def binary_search_insertion_right(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            i = m + 1

    return j



import unittest

class TestBinarySearchInsertion(unittest.TestCase):
    def test_binary_search_insertion_simple(self):
        # 测试目标值存在于列表中
        nums = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual(binary_search_insertion_simple(nums, target), 2)

        # 测试目标值不存在于列表中，且应插入到列表中间
        nums = [1, 3, 5, 7, 9]
        target = 4
        self.assertEqual(binary_search_insertion_simple(nums, target), 2)

        # 测试目标值不存在于列表中，且应插入到列表头部
        nums = [1, 3, 5, 7, 9]
        target = 0
        self.assertEqual(binary_search_insertion_simple(nums, target), 0)

        # 测试目标值不存在于列表中，且应插入到列表尾部
        nums = [1, 3, 5, 7, 9]
        target = 10
        self.assertEqual(binary_search_insertion_simple(nums, target), 5)

        # 测试空列表
        nums = []
        target = 5
        self.assertEqual(binary_search_insertion_simple(nums, target), 0)

        # 测试列表中只有一个元素，目标值等于该元素
        nums = [5]
        target = 5
        self.assertEqual(binary_search_insertion_simple(nums, target), 0)

        # 测试列表中只有一个元素，目标值小于该元素
        nums = [5]
        target = 3
        self.assertEqual(binary_search_insertion_simple(nums, target), 0)

        # 测试列表中只有一个元素，目标值大于该元素
        nums = [5]
        target = 7
        self.assertEqual(binary_search_insertion_simple(nums, target), 1)

    def test_binary_search_insertion(self):
        # 测试目标值存在于列表中
        nums = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual(binary_search_insertion(nums, target), 2)

        # 测试目标值不存在于列表中，且应插入到列表中间
        nums = [1, 3, 5, 7, 9]
        target = 4
        self.assertEqual(binary_search_insertion(nums, target), 2)

        # 测试目标值不存在于列表中，且应插入到列表头部
        nums = [1, 3, 5, 7, 9]
        target = 0
        self.assertEqual(binary_search_insertion(nums, target), 0)

        # 测试目标值不存在于列表中，且应插入到列表尾部
        nums = [1, 3, 5, 7, 9]
        target = 10
        self.assertEqual(binary_search_insertion(nums, target), 5)

        # 测试空列表
        nums = []
        target = 5
        self.assertEqual(binary_search_insertion(nums, target), 0)

        # 测试列表中只有一个元素，目标值等于该元素
        nums = [5]
        target = 5
        self.assertEqual(binary_search_insertion(nums, target), 0)

        # 测试列表中只有一个元素，目标值小于该元素
        nums = [5]
        target = 3
        self.assertEqual(binary_search_insertion(nums, target), 0)

        # 测试列表中只有一个元素，目标值大于该元素
        nums = [5]
        target = 7
        self.assertEqual(binary_search_insertion(nums, target), 1)

if __name__ == '__main__':
    unittest.main()
