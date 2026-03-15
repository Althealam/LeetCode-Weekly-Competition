# [9, 7, 5, 10, 1] ==> [9, -2, -2, 5, 9] 
# [1, 2, 6, 7] ==> [1, 1, 4, 1] 

# difference[i] = array[i]-array[i-1]
# array[i] = array[i]-array[i-1]+array[i-1]+array[i-2]+...+array[2]-array[1]+array[1]-array[0]+array[0]
# array[i] = difference[i]+difference[i-1]+...+difference[0]
 
 # diff[i] = array[i]-array[i-1], diff[i+1] = array[i+1]-array[i]

# 目标是将左右两边本来已经是等差的两段，拼接成一段

class Solution:
    def longestArithmetic(self, nums) -> int:
        n = len(nums)
        if n<=2:
            return n
        
        # 1. diff array
        diff = [nums[i]-nums[i-1] for i in range(1, n)]
        m = n-1

        # 2. left array
        left = [1]*m
        for i in range(1, m):
            if diff[i]==diff[i-1]:
                left[i] = left[i-1]+1
        
        # 3. right array
        right = [1]*m
        for i in range(m-2, -1, -1):
            if diff[i] == diff[i+1]:
                right[i] = right[i+1]+1
        
        ans = max(left)+1

        # 4. 修改中间元素
        for i in range(1, n-1):
            if (nums[i+1]-nums[i-1])%2==0:
                d = (nums[i+1]-nums[i-1])//2
                l = 0
                r = 0
                if i-1>=1 and diff[i-1]==d:
                    l = left[i-1]
                else:
                    l = 1
                
                if i<m and diff[i]==d:
                    r = right[i]
                else:
                    r = 1
                
                ans = max(ans, l+r+1)

        # 修改边界
        ans = max(ans, right[0]+1)
        ans = max(ans, left[m-1]+1)
        return ans
        



sol = Solution()
nums = [9, 7, 5, 10, 1]
res = sol.longestArithmetic(nums)
print(res)