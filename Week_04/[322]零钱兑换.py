# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划
"""
贪心 + 回溯(DFS)
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def __init__(self):
        self.res = -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        coins = sorted(coins, reverse=True)
        coins_size = len(coins)
        self.res = amount + 1

        def _coin_change(remainder, i, counter):
            if i > coins_size - 1:
                return
            num = remainder // coins[i]
            for k in range(num, -1, -1):
                _remainder = remainder - k * coins[i]
                _counter = counter + k
                if _remainder == 0:
                    self.res = min(_counter, self.res)
                    return
                if _counter > self.res:
                    break
                _coin_change(_remainder, i + 1, _counter)

        _coin_change(amount, 0, 0)

        return self.res if self.res != amount + 1 else -1


if __name__ == "__main__":
    solution = Solution()
    coins, amount = [1,2,5], 11
    s = solution.coinChange(coins, amount)
    a = 1

        
# leetcode submit region end(Prohibit modification and deletion)
