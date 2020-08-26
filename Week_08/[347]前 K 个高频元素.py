# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        nums = [(num, freq) for num, freq in Counter(nums).items()]

        def get_topk(start, end, k):
            if start >= end:
                return nums[:k]
            p = partition(start, end)
            if p == k - 1:
                return nums[:k]
            elif p < k - 1:
                return get_topk(p + 1, end, k)
            else:
                return get_topk(start, p - 1, k)

        def partition(start, end):
            pivot = nums[start]
            while start < end:
                while nums[end][-1] <= pivot[-1] and start < end:
                    end -= 1
                nums[start] = nums[end]
                while nums[start][-1] >= pivot[-1] and start < end:
                    start += 1
                nums[end] = nums[start]
            nums[start] = pivot
            return start

        n = len(nums)
        return [num for num, freq in  get_topk(0, n - 1, k)]

# leetcode submit region end(Prohibit modification and deletion)
