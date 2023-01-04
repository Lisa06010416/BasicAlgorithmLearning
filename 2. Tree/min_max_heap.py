import heapq
from typing import List
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""23. Merge k Sorted Lists"""
class Solution:
    """用min heap"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minheap = []
        val2index = defaultdict(list)

        for index, i_list in enumerate(lists):
            if i_list:
                minheap.append(i_list.val)
                val2index[i_list.val].append(index)
                lists[index] = lists[index].next  # 錯誤: i_list = i_list.next
        heapq.heapify(minheap)

        new_head = ListNode()
        pre_node = new_head
        while minheap:
            small_val = heapq.heappop(minheap)
            node = ListNode(val=small_val)
            pre_node.next = node
            pre_node = node

            index = val2index[small_val][0]
            val2index[small_val].pop(0)
            if lists[index]:
                new_val = lists[index].val
                val2index[new_val].append(index)
                lists[index] = lists[index].next
                heapq.heappush(minheap, new_val)

        return new_head.next


"""295. Find Median from Data Stream"""
class MedianFinder:
    """求可變數列的 mediant
    * 動態求第ｋ個小的
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []  # max k val
        self.max_heap = []  # min k/k+1 val
        self.total_num = 0

    def _add_val_in_max_heap(self, nums: int):
        heapq.heappush(self.max_heap, -nums)

    def _get_val_in_max_heap(self):
        return -heapq.heappop(self.max_heap)

    def _add_val_in_min_heap(self, nums: int):
        heapq.heappush(self.min_heap, nums)

    def _get_val_in_min_heap(self):
        return heapq.heappop(self.min_heap)

    def addNum(self, num: int) -> None:
        # 判斷輸入值得的大小，小於 maxheap top 的話 加到 maxheap 中
        # 大於於 maxheap top 的話 加到 maxheap 中
        if not self.max_heap or num < -self.max_heap[0]:
            self._add_val_in_max_heap(num)
        else:
            self._add_val_in_min_heap(num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            temp = self._get_val_in_max_heap()
            self._add_val_in_min_heap(temp)

        if len(self.max_heap) < len(self.min_heap):
            temp = self._get_val_in_min_heap()
            self._add_val_in_max_heap(temp)

        self.total_num += 1

    def findMedian(self) -> float:
        if self.total_num % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""239. Sliding Window Maximum"""
class Solution:
    def maxSlidingWindow_maxheap(self, nums: List[int], k: int) -> List[int]:
        """
        tips: 把index一起放到heap中協助判斷
        tips: heap裡面可以放廢物,拿到再刪掉
        依序把每個值放到heap內，再由heap中檢查最大值，如果最大值的index在win外則pop，直到找到win內的max_val
        O(n*log(k))
        """
        heap_list = []
        max_win_list = []
        nums_len = len(nums)
        for i in range(nums_len):
            heapq.heappush(heap_list, (-nums[i], i))
            if len(heap_list) >= k:
                while heap_list:
                    pop_n, pop_n_idx = -heap_list[0][0], heap_list[0][1]
                    if pop_n_idx > i-k:
                        max_win_list.append(pop_n)
                        break
                    else:
                        heapq.heappop(heap_list)
        return max_win_list


"""313. Super Ugly Number"""
class Solution:
    """題目要求找出第n個ugly number
       ugly number的定義是一個數的prime factors只有primes裡面給的數值
    """
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        min heap
        primes = [2,3,5]
        urgly_number_sep = [1, 2, 3, 4, 6]
        (2)  *2, 2^2, *2^2, 2^3
        (3)   3,  *3,  3^2, 3^2
        (5)   4,   4,   *4, 4^2
        可以看到每次要選的都是3者中的最小值(有*者)，把最小值由min heap中pop出來（一樣的值要全部一起拿出來），在將旗下一個數值放入，重複n次
        """
        urgly_number_sep = [1]

        candidate = [(p, p, 0) for p in primes]  # (value, prime, time)
        heapq.heapify(candidate)

        while len(urgly_number_sep) < n:
            min_value = candidate[0][0]
            urgly_number_sep.append(min_value)
            while candidate[0][0] == min_value:
                value, prime, time = heapq.heappop(candidate)
                heapq.heappush(candidate, (prime * (urgly_number_sep[time + 1]), prime, time + 1))
        return urgly_number_sep[-1]


"""218. The Skyline Problem"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        """
        # 開始跟結束點都是要確認的
        candidate_points = buildings.copy()
        for b in buildings:
            candidate_points.append([b[1], b[1], 0])
        candidate_points.sort() 
        
        # 動態加入目前的點以及判斷該點的答案
        heapb = []
        b_idx = 0
        res = []
        while b_idx < len(candidate_points):
            b = candidate_points[b_idx]
            heapq.heappush(heapb, (-b[2], b[0], b[1])) # 放入目前的點
            b_idx += 1
            
            # 下一個點如果位子跟目前一樣 則先將點都放入heap
            if b_idx < len(candidate_points) and candidate_points[b_idx][0] == b[0]:
                continue
            
            while heapb and heapb[0][2] <= b[0]: # 如果heap中的點已經結束則移除
                heapq.heappop(heapb)
            
            if heapb: # x不在答案內 取目前最高者
                if not res or -heapb[0][0] != res[-1][1]: 
                    res.append([b[0], -heapb[0][0]])
            else: # 沒有點 但是有要檢查的點 --> 某個building的結束
                res.append([b[0], 0])
            
        return res