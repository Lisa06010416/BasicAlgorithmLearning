# Search

## Binary Search
* 參考資料：
    * [LeetCode Binary Search Summary 二分搜索法小結](https://www.cnblogs.com/grandyang/p/6854825.html)
* **題型:**
    * type1 - 找到目標值
    * type2 - 找到第一個比目標值 小於/大於等於、小於等於/大於 的值(目標值可能不存在)
        * 小於/大於等於
            ```
                def binary_search(self, nums: List[int], target: int) -> int:
                     left, right = 0, len(nums)-1
                     while left <= right:
                         mid = left + (right-left)//2
                         if nums[mid] < target:
                             left = mid + 1
                         else:
                             right = mid - 1
                     return right # 小於
                     # return right + 1 # 大於等於 == return left
            ```
        * 小於等於/大於
            ```
                def binary_search(self, nums: List[int], target: int) -> int:
                     left, right = 0, len(nums)-1
                     while left <= right:
                         mid = left + (right-left)//2
                         if nums[mid] <= target:
                             left = mid + 1
                         else:
                             right = mid - 1
                     return right # 小於等於
                     # return right + 1 # 大於
            ```
              
    * type3 - 需要由其他函數來判斷移動mid point的方式
    * type4 - 特殊題
    

* **常見應用**:
    * search insert position
    * sqrt(n)
    * 
    
    
