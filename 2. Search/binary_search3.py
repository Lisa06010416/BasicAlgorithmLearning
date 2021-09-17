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
    """Give a array og intergers, has n+1 items, and each val in between 1~n,
    There is only on repeated number, please find out the number
    限制 : 不可以改變輸入的組數，也只能用 constant extra space (不可以用sort)
    solution 1: 鴿籠原理 + binary search O(nlogn)
    solution 2: Bit Manipulation
    solution 3: fast/low point (不是常數的空間)
    solution 4: sort and find repeat (會改變nums)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        """ 鴿籠原理 + binary search
        任意 nums 中的數字 m, 如果m不重複則組數中小於等於m的數的數量為m
        用binary search去找剛好會讓mid>count的數
        n = [1,2,3,4,4]
        low, hight = 1, 4
        mid =   2, 3, 4
        count = 2, 3, 5
        low =   3, 4, 4
        hight = 4, 4, 4 => break

        n = [1,3,4,2,2]
        low, hight = 1, 4
        mid =   2, 1
        count = 3, 1
        low =   1, 2
        hight = 2, 2 => break
        """

        low, hight = 1, len(nums) - 1
        while (low < hight):
            mid = low + (hight - low) // 2

            # nums中小於等於m的值的數量
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            # count = sum([i<=mid for i in nums]) # 比較慢

            # 移動指針
            if count <= mid:  # nums中比mid少的數小於mid個，重複的在右邊
                low = mid + 1
            else:
                hight = mid
        return low
