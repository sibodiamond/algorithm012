# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  示例: 
# 
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6 
#  Related Topics 栈 数组 哈希表 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] 表示以matrix[i][j]为最底点j列的最大柱形面积
        dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == '1':
        #             dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + 1
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + 1
                if j == 0 and dp[i][j] > 0:
                    max_area = max(max_area, dp[i][j])
                elif j > 0:
                    min_h = dp[i][j]
                    for k in range(j, -1, -1):
                        if dp[i][k] > 0:
                            wd = j - k + 1
                            min_h = min(min_h, dp[i][k])
                            max_area = max(max_area, wd * min_h)
                        else:
                            break
        return max_area









# leetcode submit region end(Prohibit modification and deletion)
