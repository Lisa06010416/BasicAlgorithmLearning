"""特殊題"""
from typing import List



""" 300. Longest Increasing Subsequence """
class Solution:
    """ 找到最長的 strictly longest Subsequence
    1. 暴力解 n**2
    2. DP 由最後一個開始判斷，前一個值如果小於後一個值則繼承前一個的dp值＋1，大於的話重新判斷 => n**2
    3. binary search => nlogn, 很難想QAQ , !!最後temp裡的序列不會是LIS,只是數量一樣
    """
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        """ binary search """
        temp = []  # 初始化一個temp
        for num in nums:
            if not temp: # temp 為空則直接加入值
                temp.append(num)
            else:
                # !! 不是嚴格遞增的話要找 大於 num 的 最小值
                index = self.binary_search(temp, num) # 找到temp內 大於等於 num 的最小值
                if index >= len(temp): # num 比目前的值都大 ， 加入temp
                    temp.append(num)
                else:  # 替換找到的值
                    temp[index] = num
        return len(temp)