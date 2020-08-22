# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#  
# 
#  示例: 
# 
#  输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"] 
# 
#  说明: 
# 你可以假设所有输入都由小写字母 a-z 组成。 
# 
#  提示: 
# 
#  
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？ 
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。 
#  
#  Related Topics 字典树 回溯算法

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board or not board[0]:
            return []
        trie, m, n, res = {}, len(board), len(board[0]), set()
        for word in words:
            tree = trie
            for c in word:
                tree = tree.setdefault(c, {})
            tree['#'] = '#'

        def dfs(i, j, tree, path):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] not in tree or board[i][j] == '*':
                return
            board[i][j], cur_char = '*', board[i][j]
            path += cur_char
            tree = tree[cur_char]
            if '#' in tree: res.add(path[:])
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = i + x, j + y
                dfs(next_i, next_j, tree, path)
            board[i][j] = cur_char

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie, '')
        return list(res)
            

# leetcode submit region end(Prohibit modification and deletion)
