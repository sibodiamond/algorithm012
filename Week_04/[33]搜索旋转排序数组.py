# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        def binary_search(nums, start, end, target):
            if start > end:
                return -1
            if start == end:
                return start if target == nums[start] else -1
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            # 左旋转，右升序
            if nums[start] > nums[mid]:
                if target > nums[mid]:
                    if target > nums[end]:
                        return binary_search(nums, start, mid - 1, target)
                    else:
                        return binary_search(nums, mid + 1, end, target)
                else:
                    return binary_search(nums, start, mid - 1, target)
            # 左升序， 右旋转
            else:
                if target < nums[mid]:
                    if target < nums[start]:
                        return binary_search(nums, mid + 1, end, target)
                    else:
                        return binary_search(nums, start, mid - 1, target)
                else:
                    return binary_search(nums, mid + 1, end, target)

        return binary_search(nums, 0, len(nums) - 1, target)













# leetcode submit region end(Prohibit modification and deletion)
