# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。 
# 
#  注意: 
# 数组长度 n 满足以下条件: 
# 
#  
#  1 ≤ n ≤ 1000 
#  1 ≤ m ≤ min(50, n) 
#  
# 
#  示例: 
# 
#  
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#  
#  Related Topics 二分查找 动态规划

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 二分查找
    def splitArray1(self, nums: List[int], m: int) -> int:
        if not nums or not m:
            return 0

        def _split(nums, max_internal_sum):
            split, tmp = 1, 0
            for num in nums:
                if tmp + num > max_internal_sum:
                    split += 1
                    tmp = 0
                tmp += num
            return split
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right + left) // 2
            count = _split(nums, mid)
            if count > m:
                left = mid + 1
            else:
                right = mid
        return left

    # 动态规划
    # 时间复杂度：O(n^2 * m)
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums or not m:
            return 0
        n = len(nums)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] += pre_sum[i - 1] + nums[i - 1]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], pre_sum[i] - pre_sum[k]))

        return dp[n][m]



















        
# leetcode submit region end(Prohibit modification and deletion)
