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


class Solution:
    """由nums中回傳最長的subset，構成subset的條件是
         answer[i] % answer[j] == 0
         answer[j] % answer[i] == 0
    """

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        DP 一個帶一個的感覺（？

        input :
        [1, 2, 3]

        dp存符合條件的數量
        dp[i] :  stored the max number of elemem can divide nums[i] with no remainder
            dp[0] = 0
            dp[1] = 1
            dp[2] = 1

        parent存可以整除自己的上一個元素的index
        parent[i] : store the previous index of nums(in the same subset)
             parent[0] = 0
             parent[1] = 0
             parent[2] = 0


        loop:
        i -> 1, j -> 2
        i -> 1, j -> 3
        i -> 2, j -> 3

        """
        if not nums:
            return []
        nums = sorted(nums)

        dp = [0] * len(nums)
        parent = [-1] * len(nums)
        max_num = 0
        max_index = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    parent[j] = i
                    if dp[j] > max_num:
                        max_num = dp[j]
                        max_index = j

        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = parent[max_index]
        return ans




