# 目标：移除前缀使得数组严格递增->找到最小下标可以让后缀严格递增->找到严格递增的连续子数组的最小下标->从后往前遍历，找到连续数组的终止下标即可
# 找到严格递增的连续子数组的最小下标
# 思路：从后往前遍历，如果nums[i-1]<nums[i]，说明[i-1, i]是递增的，那么继续移动ans指针
class Solution:
    def minimumPrefixLength(self, nums) -> int:
        ans = float('inf')
        for i in range(len(nums)-1, -1, -1):
            if i>0 and nums[i]>nums[i-1]: # 直到到达i-1都是递增的
                ans = min(ans, i-1)
            elif i==len(nums)-1 and nums[i]<nums[i-1]:
                return len(nums)-1
            else:
                break
        return ans if ans!=float('inf') else 0
                
                
nums = [1,2,3,4]
solution = Solution()
res = solution.minimumPrefixLength(nums)
print(res)