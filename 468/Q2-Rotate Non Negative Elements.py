# 1. 记录非负元素的位置
# 2. 旋转非负元素
# 3. 将非负元素放回原数组里面
from typing import Any


class Solution:
    def rotateElements(self, nums, k: int):
        # Step1: 找到非负元素的位置
        # 非负元素的值
        position_pos_num = [num for num in nums if num>=0]
        # 非负元素的下标
        position_pos_index = [x for x, num in enumerate[Any](nums) if num>=0]
        
        if len(position_pos_num)==0:
            return nums
        # Step2: 左旋数组=将最左边的K个元素，整体搬到数组的末尾（顺序不变）
        k = k%len(position_pos_num)
        position_pos_num = position_pos_num[k:]+position_pos_num[:k]

        # Step3: 将非负元素放回数组里面
        for i in range(len(position_pos_index)):
            nums[position_pos_index[i]] = position_pos_num[i]
        return nums
    
nums = [5, 4, -9, 6]
solution = Solution()
res = solution.rotateElements(nums, 2)
print(res)