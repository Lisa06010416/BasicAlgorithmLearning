from typing import List

"""152. Maximum Product Subarray"""
class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        """找到input組數中，連乘最大的subarray，返回最大值
        同時紀錄最大值跟最小值，可以用空間壓縮
        """
        local_max, local_min = nums[0], nums[0]
        global_max = nums[0]
        for n in nums[1:]:
            temp_vals = [n, local_max * n, local_min * n]
            local_max = max(temp_vals)
            local_min = min(temp_vals)
            # print(local_max, local_min)
            global_max = max(global_max, local_max)
        return global_max
