"""特殊題"""
import math
from typing import List


"""
相當於種告要找Ｋ個數（Ｋ是中位數）
分別在兩個主數中找Ｋ//2的數
"""
def get_kth(nums1, nums2, k):
    i, j = 0, 0
    while True:
        # 如果某一個組數已經走到底，可以直接在賃一個組數中找到中位數
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]

        # 剩下一個數要找
        if (k == 1):
            return min(nums1[i], nums2[j])

        # nums1 再往下移 k // 2 的數
        midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float("inf")
        # nums2 再往下移 k // 2 的數
        midVal2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float("inf")

        # 比較小個跟新index(因為Ｋ不在此)
        if midVal1 > midVal2:
            j = j + k // 2
        else:
            i = i + k // 2

        k = k - k // 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 處理中位數奇偶的球髮不同的問題
        k_left = math.ceil((len(nums1) + len(nums2)) / 2)
        k_right = math.ceil((len(nums1) + len(nums2) + 1) / 2)
        return (get_kth(nums1, nums2, k_left) + get_kth(nums1, nums2, k_right)) / 2

""" 300. Longest Increasing Subsequence """
class Solution:
    """ 找到最長的 strictly longest Subsequence
    1. 暴力解 n**2
    2. DP 由最後一個開始判斷，前一個值如果小於後一個值則繼承前一個的dp值＋1，大於的話重新判斷 => n**2
    3. binary search => nlogn !!最後temp裡的序列不會是LIS,只是數量一樣
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