# 让我们一起来玩扫雷游戏！ 
# 
#  给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）
# 地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。 
# 
#  现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板： 
# 
#  
#  如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。 
#  如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。 
#  如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。 
#  如果在此次点击中，若无更多方块可被揭露，则返回面板。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 
# 
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  示例 2： 
# 
#  输入: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  
# 
#  注意： 
# 
#  
#  输入矩阵的宽和高的范围为 [1,50]。 
#  点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。 
#  输入面板不会是游戏结束的状态（即有地雷已被挖出）。 
#  简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。 
#  
#  Related Topics 深度优先搜索 广度优先搜索

import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        rows, cols = len(board), len(board[0])

        def neighbor(r, c):
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if (dr or dc) and 0 <= r + dr < rows and 0 <= c + dc < cols:
                        yield r + dr, c + dc

        def dfs(x, y):
            neighbors = sum(board[r][c] in str('MX') for r, c in neighbor(x, y))
            if neighbors > 0:
                board[x][y] = str(neighbors)
                return
            elif board[x][y] == 'M':
                board[x][y] = 'X'
                return
            elif board[x][y] == 'E':
                board[x][y] = 'B'
                for r, c in neighbor(x, y):
                    dfs(r, c)

        def bfs(x, y):
            queue = collections.deque([(x, y)])
            visited = set([(x, y)])
            while queue:
                size = len(queue)
                for i in range(size):
                    r, c = queue.popleft()
                    if board[r][c] == 'M':
                        board[r][c] = 'X'
                    counts = sum(board[x][y] in 'MX' for x, y in neighbor(r, c))
                    if counts > 0:
                        board[r][c] = str(counts)
                    elif board[r][c] == 'E':
                        board[r][c] = 'B'
                        for x, y in neighbor(r, c):
                            if (x, y) not in visited:
                                queue.append((x, y))
                                visited.add((x, y))
        # dfs(click[0], click[1])
        bfs(click[0], click[1])
        return board


















        
# leetcode submit region end(Prohibit modification and deletion)
