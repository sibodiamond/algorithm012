# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    """
    解码个数的问题，如同路径个数的问题；
    路径问题中，初始化起始点之前位置为0，意味着在起始点之前，本无路；
    初始化通过起始点位置的路径条数为1，意味着此路是通的，并且有可能衍生出多条路径。
    """
    def __init__(self):
        self.memo = {}

    def numDecodings1(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 9 < int(s[i-1:i+1]) < 27:
                dp[i] += dp[i - 2] if i > 1 else 1
        return dp[n - 1]

    def numDecodings2(self, s: str) -> int:
        # 初始值y=1意味着s是‘一条通路’,并且可以由此路衍生出其他路径(其他序列);
        # 初始值y=0意味着s是不通的，不可以构成路径，也就是无法生成(映射)序列.
        if not s: return 0
        x, y = 0, int(s[0] > '0')
        pre = ''
        for cur in s:
            x, y = y, (cur > '0') * y + (9 < int(pre + cur) < 27) * x
            pre = cur
        return y

    # 深度优先遍历
    @lru_cache()
    def numDecodings3(self, s: str) -> int:
        if s is None: return 0
        if len(s) == 0:
            return 1
        cnt = 0
        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if len(s) > 1 and 9 < int(s[:2]) < 27:
            cnt += self.numDecodings(s[2:])
        return cnt

    def numDecodings(self, s: str) -> int:
        if s is None: return 0
        if len(s) == 0:
            return 1
        cnt = 0
        if s[0] != '0':
            if s[1:] not in self.memo:
                cnt += self.numDecodings(s[1:])
                self.memo[s[1:]] = cnt
            else:
                cnt += self.memo[s[1:]]
        if len(s) > 1 and 9 < int(s[:2]) < 27:
            if s[2:] not in self.memo:
                self.memo[s[2:]] = self.numDecodings(s[2:])
                cnt += self.numDecodings(s[2:])
            else:
                cnt += self.memo[s[2:]]
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
