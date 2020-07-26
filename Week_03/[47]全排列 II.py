# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Any


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seq, res, nums_len = [], [], len(nums)

        def backtrack(j=0):
            for i in range(0, nums_len - j):
                if nums[i] == nums[nums_len - j - 1]:
                    continue
                nums[i], nums[nums_len - j - 1] = nums[nums_len - j - 1], nums[i]
                if j + 1 == nums_len:
                    res.append(nums[:])
                else:
                    backtrack(j + 1)
                nums[i], nums[nums_len - j - 1] = nums[nums_len - j -1], nums[i]
        backtrack()
        return [list(seq) for seq in res]


# leetcode submit region end(Prohibit modification and deletion)
