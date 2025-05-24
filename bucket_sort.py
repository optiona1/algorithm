def bucket_sort(nums: list[float]):
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]
    for num in nums:
        i = int(num * k)
        bucket[i].append(num)

    for bucket in buckets:
        bucket.sort()

    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1
