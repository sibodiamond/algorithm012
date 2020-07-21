# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。 
# 
#  
# 
#  示例： 
# 
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 8 
#  
#  Related Topics 树 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def _generate(start, end):
            # terminator
            if start > end:
                return [None]
            # process & drill down
            all_trees = []
            for i in range(start, end + 1):
                left_trees = _generate(start, i - 1)
                right_trees = _generate(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        cur_node = TreeNode(i, l, r)
                        all_trees.append(cur_node)
            return all_trees
        return _generate(1, n) if n else []
# leetcode submit region end(Prohibit modification and deletion)
