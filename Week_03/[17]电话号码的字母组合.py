# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # import collections
        # digit_char = collections.defaultdict(list)
        # for i in range(2, 10):
        #     if i < 7:
        #         digit_char[str(i)] = [chr(ord('a') + (i - 2) * 3 + j) for j in range(3)]
        #     elif i == 7:
        #         digit_char[str(i)] = [chr(ord('a') + (i - 2) * 3 + j) for j in range(4)]
        #     elif i == 8:
        #         digit_char[str(i)] = [chr(ord('a') + 19 + j) for j in range(3)]
        #     else:
        #         digit_char[str(i)] = [chr(ord('a') + 22 + j) for j in range(4)]
        # print(digit_char)
        digit_char = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        if not digits:
            return []

        def backtrace(j=0, seq=''):
            for c in digit_char[digits[j]]:
                seq += c
                if j + 1 == len(digits):
                    res.append(seq)
                else:
                    backtrace(j + 1, seq)
                seq = seq[:-1]
        backtrace()
        return res

# leetcode submit region end(Prohibit modification and deletion)
