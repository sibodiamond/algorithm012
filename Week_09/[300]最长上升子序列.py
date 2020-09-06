# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    动态规划
    时间复杂度：O(n ^ 2)
    """
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp[i]表示nums[0...i]包含nums[i]可以构成最长上升子序列的长度；
        # 也就是nums[0...i]中小于或等于nums[i]的元素个数。
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    """
    贪心算法 + 二分查找
    时间复杂度：O(nlogn)
    1. tails维护的目标：
    不是最长上升子序列，而是存储：在动态地比较、生成上升子序列过程的记录；
    tails[0..i]中所存储的上升子序列长度，等于nums[0..i]客观存在的最长上升子序列长度。
    2. 每次更新tails的目标是：
    (1)当前迭代过程中的num若num大于或等于tails[length-1],
    二分查找的索引更新规则使得,最终l=length,即向上升子序列末尾添加num;
    (2)若num小于tails[lenght-1],最终会将num替换子序列中大于num元素中最小的那个值，
    这会使得：当前tails中上升子序列长度等于从零到当前迭代位置i(num的下标)的最长子序列长度的(当前替换值得操作，
    不会影响tails中记录(存储)的子列长度与真实当前位置的最长上升子序列长度的一致性)；进而，因减小上升子序列中的数值，
    而增大了在接下来的迭代过程中在tails子序列末尾添加元素的概率，使得最终tails所维护的上升子序列长度等于输入序列客观真实的
    最长上升子序列长度，虽然其子序列内容可能不是真实的最长上升子序列。
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        tails = [0] * n
        length = 0
        for num in nums:
            l, r = 0, length
            while l < r:
                mid = (l + r) >> 1
                if tails[mid] < num: l = mid + 1
                else: r = mid
            tails[l] = num
            if l == length: length += 1
        return length
        
# leetcode submit region end(Prohibit modification and deletion)
