# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    # 动态规划
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre_max, pre_min = nums[0], nums[0]
        res = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = max(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res
# leetcode submit region end(Prohibit modification and deletion)
