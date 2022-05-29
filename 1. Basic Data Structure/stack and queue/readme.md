# Stack - First in Last out

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


# Queue - First In First Out
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
    # form collections import deque
    q = deque([]) # 大部分操作跟list一樣
    q.appendleft(1)
    q.popleft(1)
  
    # queue 套件 -> multiprocess用的
    from queue import Queue
    q = Queue(maxsize=0)
    q.put('hello')
    q.get()
    q.qsize()
    q.empty()
    q.full()
    ```
* 還有一些其他功能，ex LifoQueue、PriorityQueue
* 題目：
| 題目                                         | 描述                                                         | 解法                                                         |
| -------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **239. Sliding Window Maximum**              | 給定一個組數以及窗口大小k, 返回給次窗口移動的最大值 <br>[1,3,-1,-3,5,3,6,7], 3. ->  [3,3,5,5,6,7] | 多種做法：<br>1. Nk : 每次移動窗口拾取最大值 <br/>2. multiset <br/>3. Max heap <br/>4. Deque (monotonic queue) |

