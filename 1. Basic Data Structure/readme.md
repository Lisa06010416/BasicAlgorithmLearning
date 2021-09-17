# Basic Data Structure
## Hash
把數值先記起來，之後在search時可以減少時間複雜度


## Linking List
主要是在考指針的修改 or 使用Linking List的結構減少複雜度

**題型:**
* 指針修改 ex merge/modify/insert
    * reverse
    * find mid/split link list - fast/slow point
        ```
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        ```
* 使用 Linking List 的結構減少複雜度
    * ex
        * LRU Catch - Dict + Double Linking List

**技巧:**
* new head
* fast/slow point
    * 判斷是否有環
    * 找中點

**需要注意的地方:**
* 頭尾是否有空值的問題


## Stack - First in Last out

#### Stack
前面的資訊會需要等後面的資訊才可以判斷，且會先需要比較近期才看過的資訊

**基本的stack**
可以 push pop尾 isempty top(檢查stack頂的元素)
**題目:**
* 括號匹配
* 中綴表示法/後綴表示法
* Minimum Stack 
* DFS


#### Monotone Stack
有兩種變化:
1. 比top小的值加入stack，比top大的值開始做處理 
2. 比top大的值加入stack，比top小的值開始做處理

**QP - stack 內的元素都是遞增或遞減**
    * [LeetCode Monotone stack](https://www.cnblogs.com/grandyang/p/8887985.html)  
    * [Monotone Questoin](Largest Rectangle in Histogram)


## Queue - First In First Out
可以 push pop頭 isempty peek(檢查Queue底的元素)
**Inplement:**
* circle array
**題型：**
* Queue Stack 互相轉換
    * [Implement Stack using Queues](http://glj8989332.blogspot.com/2019/09/leetcode-225-implement-stack-using.html) - push後將前面的元素都pop後在push
    * [Implement Queue using Stacks](http://glj8989332.blogspot.com/2019/09/leetcode-232-implement-queue-using.html) - pop/peek時要準備一個buffer stack，若buffer stack是空的則將值都放到buffer stack，否則返回buffer stack top的元素
* BFS

**Python Tips:**
* [Queue的3種做法](https://www.geeksforgeeks.org/queue-in-python/)
* 直接用List實作的話因為pop(0)的時間複雜度為O(n)，使用queue套件
    ```
    from queue import Queue
    q = Queue(maxsize=0)
    q.put('hello')
    q.get()
    q.qsize()
    q.empety()
    q.full()
    ```
* 還有一些其他功能，ex LifoQueue、PriorityQueue


## Min/Xax Heap
priority queue 的一種實作方法
對一個**變動的**數列，最大/最小/第Ｋ個大or小的數
題目：
* 23. Merge k Sorted Lists
* 295. Find Median from Data Stream
* 378. Kth Smallest Element in a Sorted Matrix


## Others

**continue subarray**
* 連續的值組成的subarray
    * max subarray: 
    * 求任意continue subarray的和: accum_sum
