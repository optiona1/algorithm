"""
    给定一个整数数组 nums 和一个目标元素 target ，
    请在数组中搜索“和”为 target 的两个元素，并返回它们的数组索引。
    返回任意一个解即可。
"""
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i
    return []
