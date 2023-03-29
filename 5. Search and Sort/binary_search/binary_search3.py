from typing import List

"""----------------------------- 根據給予的function做search -----------------------------"""
"""278. First Bad Version"""
def isBadVersion(n):
    return True

class Solution:
    """you have n versions [1, 2, ..., n], if version i is bad then i+1~n is bad, too
    find the first bad one
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        [1, (2), 3, 4]
        l, r, m
        1, 4, 2 -> True
        1, 2, 1 -> False
        2, 2, 2 -> True
        2, 1
        """
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return right + 1


"""----------------------------- 根據連續的 nums[mid] 比較要如何移動 -----------------------------"""
class Solution:
    """ 找到給予的array nums中最大的element的index
    nums = [1,2,3,1] => 2
    """

    def findPeakElement(self, nums: List[int]) -> int:
        """ binary search"""

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if (mid + 1) < len(nums) and nums[mid] <= nums[mid + 1]:  # peak at the right side
                left = mid + 1
            else:  # peak at the left side
                right = mid - 1
        return left


"""852. Peak Index in a Mountain Array"""
class Solution:
    """
    the input is a mountain array, and get the mounr idx
    1. arr.length >= 3
    2. There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]

    """
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[mid + 1]:  # 根據連續的 nums[mid] 比較要如何移動
                left = mid + 1
            else:
                right = mid - 1
        return right + 1


"""----------------------------- 根據條件在連續的數列上坐binary search -----------------------------"""
"""287. Find the Duplicate Number"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 鴿籠原理 + binary search
        任意 1-N 中的數字 m, 如果m不重複則組數中小於等於m的數的數量為m
        如果nums中小於等於m的數字大於m個->重複的數字小於m
        如果nums中小於等於m的數字小魚等於m個->重複的數字大於m
        """
        low, hight = 1, len(nums) - 1  # 不是對nums做bunary search，而是對1-N做binary search
        while (low < hight):
            mid = low + (hight - low) // 2
            # nums中小於等於m的值的數量
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            # 移動指針
            if count <= mid:  # nums中比mid少的數小於mid個，重複數字比m大
                low = mid + 1
            else:
                hight = mid
        return low


"""378. Kth Smallest Element in a Sorted Matrix"""
"""
給一個矩陣其中每列每行各自按照升序排序。回傳矩陣中第 k 小的元素。
Input: matrix = [[ 1, 5, 9],
                 [10,11,13],
                 [12,13,15]] 
       k = 8 
Output: 13

1. heap
2. BST:
    left = matrix[0][0] # 最小的元素
    right = matrix[-1][-1] # 最大的元素
    判斷matrix中比mid小於等於的元素有多少個，如果小於Ｋ則 left = mid+1，如果大於Ｋ則 right = mid-1
        * 判斷matrix中比mid小於等於的元素有多少個 -> 使用sorted matrix的特性
            * 由右上角開始 判斷該行有幾個元素小於mid，接下來再往下一移動一個index
            left=1, right=15, mid=8
            [[ 1,  (5),  (9)], => 2個
             [(10),(11), 13 ], => 0個
             [ 12,  13,  15 ]] => 0個
"""
class Solution:
    def count_small_element_num(self, matrix, target):
        x, y = 0, len(matrix[0]) - 1
        s_num = 0
        max_val = float("-inf")
        while x < len(matrix) and y >= 0:
            if matrix[x][y] <= target:
                s_num += (y + 1)
                max_val = max(matrix[x][y], max_val)
                x += 1
            else:
                y -= 1
        return s_num

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        left, right = matrix[0][0], matrix[-1][-1]

        while left <= right:
            mid = left + (right - left) // 2

            k_smaller = self.count_small_element_num(matrix, mid)

            if k_smaller < k:
                left = mid + 1
            else:
                right = mid - 1
        return left


