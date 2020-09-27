from typing import List
import random
random.seed(2020)
class QuickSort:
    def __init__(self, nums: List):
        self.nums = nums

    def sort(self, ascent=True):
        nums_len = len(self.nums)
        self.quick_sort(self.nums, 0, nums_len-1, ascent=ascent)

    def quick_sort(self, nums, start, end, ascent=True):
        if start >= end:
            return
        if ascent:
            pirot = self.partition_ascent(nums, start, end)
        else:
            pirot = self.partition_descent(nums, start, end)
        self.quick_sort(nums, start, pirot - 1, ascent)
        self.quick_sort(nums, pirot + 1, end, ascent)

    def partition_ascent(self, nums, start, end):
        # if start == end:
        #     return start
        pirot = random.randint(start, end)
        # 将随机选取的比较值置于数组两端，对于升序，起始位置的值被作为比较值，并且该位置将被新值更新覆盖，
        # 最后将比较值放入正确序列的位置
        nums[pirot], nums[start] = nums[start], nums[pirot]
        tmp = nums[start]
        while start < end:
            while nums[end] >= tmp and start < end:
                end -= 1
            nums[start] = nums[end]
            while nums[start] <= tmp and start < end:
                start += 1
            nums[end] = nums[start]
        nums[start] = tmp
        return end

    def partition_descent(self, nums, start, end):
        if start == end:
            return start
        pirot = random.randint(start, end)
        nums[end], nums[pirot] = nums[pirot], nums[end]
        tmp = nums[end]
        while start < end:
            while start < end and nums[start] >= tmp:
                start += 1
            nums[end] = nums[start]
            while start < end and nums[end] <= tmp:
                end -= 1
            nums[start] = nums[end]
        # nums[end] = tmp
        nums[start] = tmp
        return start


def quick_sort(nums, start, end, ascent=True):
    if start >= end:
        return
    if ascent:
        # pirot = partition_ascent(nums, start, end)
        pirot = partition(nums, start, end)
    else:
        pirot = partition_descent(nums, start, end)
    quick_sort(nums, start, pirot - 1, ascent)
    quick_sort(nums, pirot + 1, end, ascent)


def partition_ascent(nums, start, end):
    pirot = random.randint(start, end)
    # 将随机选取的比较值置于数组两端，对于升序，起始位置的值被作为比较值，并且该位置将被新值更新覆盖
    # 最后将比较值放入升序排序的正确位置
    nums[pirot], nums[start] = nums[start], nums[pirot]
    tmp = nums[start]
    while start < end:
        while nums[end] >= tmp and start < end:
            end -= 1
        nums[start] = nums[end]
        while nums[start] <= tmp and start < end:
            start += 1
        nums[end] = nums[start]
    nums[start] = tmp
    return end


def partition_descent(nums, start, end):
    if start == end:
        return start
    pirot = random.randint(start, end)
    nums[end], nums[pirot] = nums[pirot], nums[end]
    tmp = nums[end]
    while start < end:
        while start < end and nums[start] >= tmp:
            start += 1
        nums[end] = nums[start]
        while start < end and nums[end] <= tmp:
            end -= 1
        nums[start] = nums[end]
    nums[end] = tmp
    return start


def partition(nums, start, end):
    pivot, cnt = end, start
    for i in range(start, end):
        if nums[i] > nums[pivot]:
            nums[cnt], nums[i] = nums[i], nums[cnt]
            cnt += 1
    nums[cnt], nums[pivot] = nums[pivot], nums[cnt]
    return cnt


if __name__ == "__main__":
    import random
    nums = [6, 8, 3, 10, 2, 34, 22, 15]
    nums = [1, 2, 2, 1, 1]
    nums = [random.randint(1, 100) for _ in range(10)]
    print(nums)
    pivot = partition(nums, 0, len(nums) - 1)
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
    # qs = QuickSort(nums)
    #
    # qs.sort(False)
    # a = 1





