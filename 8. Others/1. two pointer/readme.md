# Two Point

* **題型：**
    * 通常要in-place的做什麼事的時候
    * 在處理一組sorted的array/linkinglist時，要找滿足特定條件的element時，可能會要用two point，element可能是一個值，一個triplet，一個subarray等

* **題目:**
    * in-place (ex merge/delete duplicate in list)
        -[ ] 
        -[ ] 
    * element 是一個值
        -[ ] 167 Two Sum II - Input array is sorted
        -[ ] 977 Squares of a Sorted Array
    * element 是一個 triplet
        -[ ] 15 3Sum
    * element 是一個 subarray - sliding windows
        -[ ] 713 Subarray Product Less Than K
    

* TIPS:
    * 跟binary search一樣都要用在已經sorted的好array上，binary search是查詢特定值，two point是查詢符合特定條件的狀況(該狀況無法沒有順序性，無法只接用mid判斷)
    * Sliding Windows 的題目也會用到two point去滑動床口