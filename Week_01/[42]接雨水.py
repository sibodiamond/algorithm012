# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        i = 0
        while i < len(height):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                low_idx = stack.pop()
                if not stack:
                    break
                hd = min(height[i], height[stack[-1]]) - height[low_idx]
                wd = i - stack[-1] - 1
                res += hd * wd
            stack.append(i)
            i += 1
        return res










# leetcode submit region end(Prohibit modification and deletion)
