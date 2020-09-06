# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。 
# 
#  一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：
# 
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  示例 2： 
# 
#  输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：
# 
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^ 
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    """
    求解两个序列，在一个序列的所有子序列中最多存在几个另一个序列；
    1. 递归思路：
    和路径个数的求解异曲同工，其根本思路基本一致；
    (1)不同的是，s序列选择的下一步可能是向后一步或者两步(目的是寻找所有题解)；要‘同步’移动s和t;
    (2)最终在s中走过的节点序列的子序列可以组成'另一个序列t'，此时t也走到终点，
    '在s中寻找与t相同的节点(也是可以解开当前t关卡的题解)完成t的每道关卡',算作一条通路(一套题解)；
    (3)在s上的移动的同时，也在t上移动，只有s找到t的当前节点(只有在s中找到当前t关卡的题解)，t才向后移动(进入下一关)；
    (4)s和t节点的判断，指导了s和t的移动步数；
    当s和t当前节点相同，
    那么意味着可以s和t都向后移动一步，“完成了前进路上的一道关卡”，进入下一关(可能找到一条通路)；
    也可以只移动s一步，在s寻找下一个与当前t相同的节点(寻找解决当前t关卡的其他题解)，
    即寻找另一条通路(另一套题解)；由于题目是返回最多的个数，也就是最大可能寻找所有可能的路径(所有题解组合)，所以，当s和t的
    当前节点相同，要进行上述两种移动。
    当s和t当前节点不同(当前s节点不是当前t的题解)，
    只有移动s一步，寻找s与当前t相同的节点(向后寻找当前t的题解)，(才能完成当前关卡)才可能最终走通。

    2. 动态规划：
    思路：通过记录解的一部分和状态转换达到全部解的记录；
    横坐标是s(i), 纵坐标是t(j)
    dp[j][i]:表示s[0..i]所有子序列中包含t[0..j]的个数
      # b a b a g b a g  
    # 1 1 1 1 1 1 1 1 1
    b 0 1 1 2 2 2 3 3 3
    a 0 0 1 1 3 3 3 6 6
    g 0 0 0 0 0 3 3 3 9
    if s[i] == t[j]: dp[j][i] = dp[j][i - 1] + dp[j - 1][i - 1]
    else: dp[j][i] = dp[j][i - 1] 
    A: 当s的当前节点和t的当前相同，s[0..j]的所有子序列包含t[0..j]的个数取决于(1)(2)
    (1)不包括当前s[i]的情况下,s[0..i-1]包含t[0..j]的个数 = dp[j][i - 1]，
    也就是，由s[0..i-1]中包含与s[i](t[i])相同的节点(可能不止一个)与其他节点(构成t[0..j - 1]子序列的节点)组成的子序列包含t[0..j]的个数
    (2)包含s[i]的情况，s[i]与s[0..i-1]构成t[0..j]的所有子序列的个数,这取决于s[0..i - 1]所有子序列包含t[0..j-1]的个数，
    dp[j - 1][i - 1]是s[0..i-1]的节点所组成的所有子序列中包含t[0..j - 1]的所有情况(个数),
    因此s的当前节点s[i]与构成t[0..j-1]的s[0..i-1]的所有子序列组合，可以构成与t[0..j]相同的序列，也就是组合出s[0..i]序列中以s[i]结尾等于
    t[0..i]的所有子序列；
    因此由(1)和(2)推理可得 => if s[i] == t[j]: dp[j][i] = dp[j][i - 1] + dp[j - 1][i - 1]
    B: 当s[i] != t[j]时，s[0..i]子序列中等于t[0..j]的个数取决于s[0..i]，如同上述情况(1)。
    因此可以推出 => if s[i] != t[j]: dp[j][i] = dp[j][i - 1] 
    
    """
    def numDistinct1(self, s: str, t: str) -> int:
        def helper(s, i, t, j, map):
            m, n = len(s), len(t)
            if i == m and j != n:
                return 0
            if j == n:
                return 1
            cnt = 0
            if s[i] == t[j]:
                k1 = '{}&{}'.format(i + 1, j + 1)
                cnt += map[k1] if k1 in map else helper(s, i + 1, t, j + 1, map)
                k3 = '{}&{}'.format(i + 1, j)
                cnt += map[k3] if k3 in map else helper(s, i + 1, t, j, map)
            else:
                k2 = '{}&{}'.format(i + 1, j)
                cnt += map[k2] if k2 in map else helper(s, i + 1, t, j, map)
            key = '{}&{}'.format(i, j)
            if key not in map:
                map[key] = cnt
            return cnt
        map = {}
        res = helper(s, 0, t, 0, map)
        return res

    # time out
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache()
        def helper(s, i, t, j):
            m, n = len(s), len(t)
            if i == m and j != n:
                return 0
            if j == n:
                return 1
            cnt = 0
            if s[i] == t[j]:
                cnt += helper(s, i + 1, t, j + 1)
                cnt += helper(s, i + 1, t, j)
            else:
                cnt += helper(s, i + 1, t, j)
            return cnt
        res = helper(s, 0, t, 0)
        return res

    def numDistinct2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if not m: return 0
        if not n: return 1
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n + 1):
            for j in range(1, m + 1):
                if i == 0:
                    dp[i][j] = 1
                elif t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[n][m]








        
# leetcode submit region end(Prohibit modification and deletion)
