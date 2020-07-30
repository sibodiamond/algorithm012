# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = -1
    # Time Limit Exceeded
    def jump_backtrace(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        nums_ln = len(nums)
        self.res = float('inf')

        O(M^N)
        def backtrace(i, counter):
            for k in range(nums[i], 0, -1):
                if i + k >= nums_ln - 1:
                    self.res = min(counter + 1, self.res)
                    return
                if counter + 1 >= self.res:
                    break
                if nums[i + k] == 0:
                    continue
                backtrace(i + k, counter + 1)

        backtrace(0, 0)

        return self.res if self.res != float('inf') else -1

    # O(n)
    # 从起点开始迈步，选择的第一步要使得第二步迈得尽可能远(接近目标)，即以此类推：
    # 选择的当前一步，要考虑使得其下一步尽可能接近目标；
    # 因此当前一步落脚点的选择都在[last_end, cur_end]， 起始点的last_end和cur_end皆为0。
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        cur_end, next_max_end, step = 0, 0, 0
        for i in range(len(nums) - 1):
            next_max_end = max(next_max_end, i + nums[i])
            if i == cur_end:
                cur_end = next_max_end
                step += 1
        return step



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,9,7,4,7,0,0,1,8,5]
    # [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    res = solution.jump(nums)
