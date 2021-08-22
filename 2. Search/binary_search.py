from typing import List


"""35. Search Insert Position"""
class Solution:
    """找看看target是否在list中，在的話回傳該target的index，不在的話回傳要insert的index
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = -1
        left = 0
        right = len(nums) - 1  # len(nums)
        has_target = False
        while left <= right:  # left < right
            mid = left + (right - left) // 2
            if nums[mid] == target:
                has_target = True
                break

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1  # right = mid
        return mid if has_target else left  # else right



"""33. Search in Rotated Sorted Array"""
class Solution:
    """ 在一個被rotated過的list中找特定值的index"""
    def search(self, nums: List[int], target: int) -> int:
        left_point = 0
        right_point = len(nums) - 1 # 如果是用減一的
        target_index = -1

        while left_point <= right_point:
            center_point = left_point + (right_point - left_point) // 2  # 則這裡比較容易拿到比較小的center
            if nums[center_point] == target:
                target_index = center_point
                break

            if nums[left_point] > nums[right_point]:
                if nums[center_point] > nums[right_point]:
                    if (target < nums[center_point]) and (target > nums[right_point]):  # 在值相等的時候要優先動 left_point
                        right_point = center_point - 1
                    else:
                        left_point = center_point + 1
                else:
                    if (target > nums[center_point]) and (target <= nums[right_point]):  # 在值相等的時候要優先動 left_point
                        left_point = center_point + 1
                    else:
                        right_point = center_point - 1
            else:
                if (target < nums[center_point]):
                    right_point = center_point - 1
                else:
                    left_point = center_point + 1

        return target_index


"""153. Find Minimum in Rotated Sorted Array"""
class Solution:
    """找一個被rotated的list中的最小值
    在不會檢查mid是否命中target的版本中，要用 right = len(nums) 的版本，避免 right = mid - 1, 在mid剛好指到最小值時錯過最小值
    """
    def findMin(self, nums: List[int]) -> int:
        # target = float("-inf")
        left = 0
        right = len(nums)
        nums.append(nums[-1]) # 多 append 最後一個值，避免後面 out of range
        while left < right:
            mid = left + (right - left)//2
            # 因為預設target是最小值，不會在nums裡面，不會有檢查target是否命中
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # 因此不能使用 mid-1 的版本，會錯過最小值
        return nums[left]


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

"""Box Stacking Problem"""
# http://web.ntnu.edu.tw/~algo/Subsequence.html#4


"""287. Find the Duplicate Number"""
class Solution:
    """Give a array og intergers, has n+1 items, and each val in between 1~n,
    There is only on repeated number, please find out the number
    限制 : 不可以改變輸入的組數，也只能用 constant extra space (不可以用sort)
    solution 1: 鴿籠原理 + binary search
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
