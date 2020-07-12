# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # i, j = 0, 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         if i != j:
        #             nums[j] = 0
        #         i += 1
        count = nums.count(0)
        nums[:] = [n for n in nums if n != 0]
        nums += [0]*count


# leetcode submit region end(Prohibit modification and deletion)
