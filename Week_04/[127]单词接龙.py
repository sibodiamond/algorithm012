# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索
import collections
# from typing import List

# alphabet = "abcdefghijklmnopqrstuvwxvz"
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    # 深度优先搜索，回溯的方式计算代价为指数级；
    # 广度优先搜索，以最先转换成目标词的步数 + 1(层数)为最小转换序列长度, 包括起始单词本身。

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        # 单词所在层数，由其产生词决定，即：产生词词层 + 1
        dequeue = collections.deque([(beginWord, 1)])
        word_len = len(beginWord)
        while dequeue:
            word, length = dequeue.popleft()
            if word == endWord:
                return length
            for i in range(word_len):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in word_set:
                        # 单词所在层数，由其产生词决定，即：产生词词层 + 1
                        dequeue.append((next_word, length + 1))
                        word_set.remove(next_word)
        return 0

    # 单向队列
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        word_size = len(beginWord)
        # 字母表易失误出错
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        step = 1
        while queue:
            queue_size = len(queue)
            while queue_size > 0:
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(word_size):
                    for c in alphabet:
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in wordList:
                            queue.append(next_word)
                            wordList.remove(next_word)
                queue_size -= 1
            step += 1
        return 0

    # 双向队列
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue1, queue2 = collections.deque([beginWord]), collections.deque([endWord])
        visited1, visited2 = set(), set()
        length, word_size = 1, len(beginWord)
        while queue1:
            if len(queue2) > len(queue1):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1
            tmp = collections.deque()
            while queue2:
                word = queue2.popleft()
                if word in queue1:
                    return length
                for i in range(word_size):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in wordList and next_word not in visited2:
                            tmp.append(next_word)
                            visited2.add(next_word)
            queue2 = tmp
            # 若其中一队列无法继续向前搜索，则意味着搜索失败
            if not queue2:
                return 0
            length += 1
        return length







# if __name__ == "__main__":
#     words = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
#     begin_word = "ymain"
#     end_word = "oecij"
#     solution = Solution()
#     k = solution.ladderLength(begin_word, end_word, words)
#     t = 1







        
# leetcode submit region end(Prohibit modification and deletion)
