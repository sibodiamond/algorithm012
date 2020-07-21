# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self._generate(0, 0, n, '', res)
        return res

    def _generate(self, left: int, right: int, n: int, s: str, res: List[str]):
        if left == n and right == n:
            res.append(s)
            return
        if left < n:
            self._generate(left+1, right, n, s+'(', res)
        if left > right:
            self._generate(left, right+1, n, s+')', res)
        return








# leetcode submit region end(Prohibit modification and deletion)
