from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""23. Merge k Sorted Lists"""
class Solution:
    """
    1. min heap
    2. merge sort
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass



"""912. Sort an Array"""
class Solution:
    # 1. Select Sort
    # 2. Insert Sort
    # 3. Bubble Sort
    # 4. merge sort
    # 5. quick sort
    # 6. heap sort

    def insert_sort(self, nums: List[int]) -> List[int]:
        sort_list = [nums[0]]
        for n in nums[1:]:
            # get insert index
            index = len(sort_list) + 1
            for i in range(len(sort_list)):
                if n <= sort_list[i]:
                    index = i
                    break
            # insert
            sort_list.insert(index, n)
        return sort_list

    def bubble_sort(self, nums: List[int]) -> List[int]:
        for time in range(1, len(nums)):
            has_swap = False
            for index in range(0, len(nums)-time):
                if nums[index] > nums[index+1]:
                    has_swap = True
                    nums[index], nums[index+1] = nums[index+1], nums[index]
            if not has_swap:
                break
        return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        def _merge_sort(nums, l, r):
            # 1. split and sort nums
            if r-l == 0:
                return
            if r-l == 1:
                if nums[r] < nums[l]:
                    nums[l], nums[r] = nums[r], nums[l]

            mid = l + (r-l)//2
            _merge_sort(nums, l, mid)
            _merge_sort(nums, mid+1, r)

            # 2. merge
            left_sub = nums[l:mid+1] + [float('inf')]
            right_sub = nums[mid+1:r+1] + [float('inf')]
            left, right = 0, 0
            while left_sub[left] != float('inf') or right_sub[right] != float('inf'):
                if left_sub[left] < right_sub[right]:
                    nums[l] = left_sub[left]
                    left+=1
                else:
                    nums[l] = right_sub[right]
                    right+=1
                l += 1
        _merge_sort(nums,0,len(nums)-1)
        return nums

    def quick_sort(self, nums: List[int]) -> List[int]:

        def _quick_sort(nums, left, right):
            if right - left <= 0:
                return

            # 為了加速，優化選p的策略 選中間數為p
            nums[right], nums[(left + right) // 2] = nums[(left + right) // 2], nums[right]

            # i 指著分界(小於nums[p]的最右邊的數)，j負責traversal整個list
            i, j = left - 1, left

            p = right  # p 是 pivot 的 index

            # 掃描list並交換人質
            while j < right:
                if nums[j] < nums[p]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1

            # 交換privot
            i += 1
            nums[i], nums[p] = nums[p], nums[i]

            _quick_sort(nums, left, i - 1)
            _quick_sort(nums, i + 1, right)

        _quick_sort(nums, 0, len(nums) - 1)
        return nums
