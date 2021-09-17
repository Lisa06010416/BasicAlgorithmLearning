from typing import List


"""26. Remove Duplicates from Sorted Array"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1, 2, 2, 3]
        """

        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left


"""88. Merge Sorted Array"""
class Solution:
    """
    Merge 兩個排序好的array - **inplace**

    相似題 :
    21. Merge Two Sorted Lists - Merge two sorted linked lists
    23. Merge k Sorted Lists - Merge k sorted linked lists (heap)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        place complex O(1), time complex O(m+n)
        """

        # ** move element in nums1 **
        for i in range(n + m - 1, n - 1, -1):
            nums1[i] = nums1[i - n]

        # merge
        p, p1, p2 = 0, n, 0
        while (p1 < m + n and m != 0) and p2 < n:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        while p2 < n:
            nums1[p] = nums2[p2]
            p2 += 1
            p += 1


"""189. Rotate Array"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]

        nums = [1,2], k = 3
        Output: [2,1]
        """

        k = k % len(nums)

        cur = 0
        pre_num = nums[0]
        start = 0
        t = 0
        while t < len(nums):
            cur = cur + k
            if cur >= len(nums):
                cur = cur - len(nums)

            pre_num, nums[cur] = nums[cur], pre_num

            if cur == start and start < k - 1:
                cur = start + 1
                pre_num = nums[cur]
                start += 1

            t += 1