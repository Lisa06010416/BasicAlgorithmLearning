"""Type2 - 找到第一個比目標值 大於等於/小於、大於/小於等於 的值(目標值可能不存在)
"""

from typing import List

"""--------------------------------- 小於/大於等於 ---------------------------------"""
"""35. Search Insert Position"""
class Solution:
    """ Search Insert Position
    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Input: nums = [1,3,5,6], target = 2
    Output: 1
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        """相當於找大於等於target的index"""
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1


"""153. Find Minimum in Rotated Sorted Array"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:  # 右半邊是有序的
                if mid >= 1 and nums[mid] > nums[mid - 1]:  # 最小值不在右邊
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 左半邊是有序的
                if nums[left] >= nums[right]:  # 最小值不在左半邊
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[right]


"""--------------------------------- 小於等於/大於 ---------------------------------"""
"""69. Sqrt(x)"""
class Solution:
    """ 求input數值的平方根
    1. binary search
    2. 牛頓迭代法

    類似題目：
    50. power(x, n)
    372. Super Pow
    """
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2

            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right


