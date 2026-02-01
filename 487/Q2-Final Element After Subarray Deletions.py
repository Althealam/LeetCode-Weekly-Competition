# 因为一次只能删除一段连续子数组，因此删到只剩下一个元素的时候，只可能剩下数组的端点元素
# 分析：题目要求删除的是一个连续子数组，并且子数组的长度不可以超过m
# 如果删除了一个连续子数组，那么剩下的可能有三种情况：
# (1) 左边一段
# (2) 右边一段
# (3) 左边和右边拼接在一起
# 假设最大元素在数组的左边或者右边的边界，那么Alice可以直接一个步骤赢的游戏
# 假设最大元素在数组的中间，那么最终会只剩下右半边的数组，然后Bob在继续进行操作

class Solution:
    def finalElement(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        return max(nums[0], nums[-1])
 
nums = [0, 5, 1, 2]
solution = Solution()
ans = solution.finalElement(nums)
print(ans)
