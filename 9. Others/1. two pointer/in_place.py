from typing import List


"""26. Remove Duplicates from Sorted Array"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1 # 要放置答案的point
        for right in range(1, len(nums)): # 遍歷判斷元素是否重複，沒有重複的話把值放到left
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left



"""334. Increasing Triplet Subsequence"""
class Solution:
    """
    是否有index i < j < k make nums[i] < nums[j] < nums[k].
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        """有趣的two-point 紀錄最小跟次小的 找到比次小大的極可以返回"""
        min_v, second_v = float('inf'), float('inf')
        for n in nums:
            if n < min_v:
                min_v = n
            elif n >  min_v and n < second_v:
                second_v = n
            elif n > second_v:
                    return True
        return False
