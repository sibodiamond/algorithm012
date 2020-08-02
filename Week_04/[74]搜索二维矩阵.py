# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        def binary_search(matrix, x1, x2, y1, y2, target):
            if target < matrix[x1][y1] or target > matrix[x2][y2]:
                return False
            if x1 == x2:
                if y1 > y2:
                    return False
                # [[x]]
                elif y1 == y2:
                    return matrix[x1][y1] == target
                mid_y = (y1 + y2) // 2
                if target == matrix[x1][mid_y]:
                    return True
                elif target > matrix[x1][mid_y]:
                    return binary_search(matrix, x1, x2, mid_y + 1, y2, target)
                else:
                    return binary_search(matrix, x1, x2, y1, mid_y - 1, target)
            mid_x = (x1 + x2) // 2
            if target == matrix[mid_x][y2]:
                return True
            elif target > matrix[mid_x][y2]:
                return binary_search(matrix, mid_x + 1, x2, y1, y2, target)
            else:
                return binary_search(matrix, x1, mid_x, y1, y2, target)

        return binary_search(matrix, 0, m - 1, 0, n - 1, target)

# leetcode submit region end(Prohibit modification and deletion)
