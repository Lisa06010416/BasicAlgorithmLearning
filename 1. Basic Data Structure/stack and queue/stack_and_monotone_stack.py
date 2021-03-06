from typing import List

""" --------------------------------- Type 1 ---------------------------------"""

""" 42 Trapping Rain Water """
class Solution(object):
   """
   # 1. Dp - 對每個格子分別找到其左右最高的牆，再去計算該格子可以累積的水量
   # 2. two point -
   # 3. monotone stack - 遞減
   """
   def trap(self, height: List[int]) -> int:
      """monotone stack"""
      monotone_stack = [(-1, 0)]
      res = 0
      for i in range(len(height)):
         if len(monotone_stack) <= 1 or height[i] <= monotone_stack[-1][1]:
            monotone_stack.append((i, height[i]))
         else:
            while monotone_stack[-1][0] != -1 and height[i] > monotone_stack[-1][1]:
               pre_index, pre_hight = monotone_stack.pop(-1)
               left_wall_index, lef_wall_high = monotone_stack[-1]
               hight = max(min(height[i], lef_wall_high) - pre_hight, 0)
               width = i - left_wall_index - 1
               res += hight * width
            monotone_stack.append((i, height[i]))
      return res

# ob = Solution()
# print(ob.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


""" --------------------------------- Type 2 ---------------------------------"""

"""82  Largest Rectangle in Histogram"""
class Solution:
   """ monotone stack - 遞增
   * 保證stack內的值越來越大
   * 當遇到比stack top還小的值的時候：
      * 第一個被pop出來的值自己組成一個rectangle
      * 第二個被pop出來的值一定可以跟第一個組成一個rectangle
      * 第三個被pop出來的值一定可以跟第一,二個組成一個rectangle
      * 直到 stack top 的值小於目前迴圈指到的值
      * 在將目前的值加入stack - 可以保證目前pop出來的值到迴圈指到的值中間的rectangle都是更大的
   * 尾端加入-1保證全部的值都會被處理到
   * 長度的算法是 (h_index-stack[-1]-1) 由目前的index到stack top 是長度 , 因此初始化 stack = [-1] 方便計算
   """
   def largestRectangleArea(self, heights: List[int]) -> int:
      heights.append(-1)
      stack = [-1]
      max_area = 0
      for h_index, h_val in enumerate(heights):
         while stack and heights[stack[-1]] > h_val:
            cur = stack.pop(-1)
            area = heights[cur] * (h_index-stack[-1]-1)
            max_area = max(max_area, area)
         stack.append(h_index)
      return max_area


"""85. Maximal Rectangle"""
class Solution:
   """
   第一種方法 monotone stack:
   1. 對每一層座長條圖，在用82  Largest Rectangle in Histogram的解法
   第二種方法:
   2. 對每一格算根據其高度，的左右邊界的index
   """
   def largestRectangleArea(self, heights: List[int]) -> int:
      heights.append(-1)
      stack = [-1]
      max_area = 0
      for h_index, h_val in enumerate(heights):
         while stack and heights[stack[-1]] > h_val:
            cur = stack.pop(-1)
            area = heights[cur] * (h_index - stack[-1] - 1)
            max_area = max(max_area, area)
         stack.append(h_index)
      return max_area

   def maximalRectangle(self, matrix: List[List[str]]) -> int:
      histogram = []
      for row_id, row in enumerate(matrix):
         temp = []
         for col_id, col in enumerate(row):
            hight = 0
            for i in range(row_id + 1):
               if matrix[row_id - i][col_id] == "1":
                  hight += 1
               else:
                  break
            temp.append(int(hight))
         histogram.append(temp)

      max_area = 0
      for row in histogram:
         area = self.largestRectangleArea(row)
         max_area = max(max_area, area)
      return max_area


""" --------------------------------- Type 3 ---------------------------------"""
# 求第i個值(被pop的)中左右分別連續大於自己的數的數量 => 遞增 stack

"""907. Sum of Subarray Minimums"""
class Solution:
   """
   題目給一個array要求每個**連續**子集中最小值的和
   以 arr = [3, 1, 2, 4]
   Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
   Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
   Sum is 17.

   1. dp
   dp_left[i] => 到第i個值時的左邊有幾個連續大於自己的值
   dp_right[i] => 到第i個值時的右邊有幾個連續大於自己的值

   2. monotone stack - 遞增
   遞增 stack 可以知道當一個值被pop時，其左邊與右邊有幾個連續大於本身的數字
   而當一個值是幾個子集的最小值的數量 = 左邊小於本身值的數量 x 右邊小於本身值的數量
   """
   def sumSubarrayMins(self, arr: List[int]) -> int:
      stack = []
      arr.append(float("-inf"))
      sum_val = 0
      for val_index, val in enumerate(arr):
         while stack and arr[stack[-1]] > val:
            cur = stack.pop(-1)
            if stack:
               left_index = stack[-1]
            else:
               left_index = -1
            sum_val += arr[cur] * (val_index - cur) * (cur - left_index)
         stack.append(val_index)
      return sum_val


"""1793. Maximum Score of a Good Subarray"""
class Solution:
   """ 跟第82題很像，只是多了一行限制 :
   if (stack[-1] + 1) <= k and (val_index - 1) >= k:
   """
   def maximumScore(self, nums: List[int], k: int) -> int:
      nums.append(-1)
      stack = [-1]
      max_score = 0
      for val_index, val in enumerate(nums):
         while stack[-1] != -1 and nums[stack[-1]] > val:
            pop_index = stack.pop(-1)
            if (stack[-1] + 1) <= k and (val_index - 1) >= k:
               score = nums[pop_index] * (val_index - stack[-1] - 1)
               max_score = max(max_score, score)
         stack.append(val_index)
      return max_score


"""1856. Maximum Subarray Min-Product"""
from itertools import accumulate
class Solution:
   """ 給予一個array，找出該array中subarray的最大min-product
   min-product: 一個array中的最小值 x 該array的和
   """
   def maxSumMinProduct(self, nums: List[int]) -> int:
      nums.append(-1)
      stack = [-1]
      max_val = 0
      accum_sum = list(accumulate(nums, initial=0))  # !! Tips
      for val_inde, val in enumerate(nums):
         while stack[-1] != -1 and val < nums[stack[-1]]:
            pop_index = stack.pop(-1)
            temp_val = nums[pop_index] * (accum_sum[val_inde] - accum_sum[stack[-1] + 1])
            max_val = max(temp_val, max_val)
         stack.append(val_inde)
      return max_val % (10 ** 9 + 7)



""" --------------------------------- Type 4 ---------------------------------"""

""" 1944. Number of Visible People in a Queue """
class Solution:
   """一群人站成一排找可以看到右邊的幾個人（任兩人中間的人都比他們矮 可以互相看到）"""
   def canSeePersonsCount(self, heights: List[int]) -> List[int]:
      heights = reversed(heights)
      stack = []
      ans = []
      for h in heights:

         n = 0
         h_index = 0
         # 可以看到幾個矮子
         for v in reversed(stack):
            if v < h:
               n += 1
               h_index += 1
            else:
               break

         # 是否可以多看到一個高的
         if h_index < len(stack):
            n += 1

         ans.append(n)
         # 如果比目前的 stack top 大 => pop
         while stack and h > stack[-1]:
            stack.pop(-1)
         stack.append(h)  # 加入自己的高度
      return reversed(ans)

