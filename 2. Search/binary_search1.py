from typing import List


"""33. Search in Rotated Sorted Array"""
class Solution:
    """在一個被rotated的nums array裡面找到target，要求時間複雜度 O(logn)"""
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search 找target的變形
        1. 中間值與最右的值可以判斷哪一半邊是有序的
        [4,5,(6),7,0,1,2] => 6 > 2 -> 左半邊是有序的
        [4,5,6,7,0,(1),2] => 1 <= 2 -> 右半邊是有序的

        2. 判斷目標值是否在有序的那半中,來看要如何移動指針
        """

        left, right = 0, len(nums) - 1  # 後面會直接比較 nums[right] 因此要減1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:  # mid > right -> 左半邊是有序的
                if target < nums[mid] and target >= nums[left]:  # 看target是否在左半邊中，判斷指針移動方式
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid < right -> 右半邊是有序的
                if target > nums[mid] and target <= nums[right]:  # 看target是否在右半邊中，判斷指針移動方式
                    left = mid + 1
                else:
                    right = mid - 1
        return -1





"""Box Stacking Problem"""
# http://web.ntnu.edu.tw/~algo/Subsequence.html#4



