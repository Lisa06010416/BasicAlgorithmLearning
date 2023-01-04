# Stack - First in Last out(FILO)

| Function    | Description                                   |
| ----------- | --------------------------------------------- |
| pop()       | Remove the top item from the stack            |
| push(iterm) | Add an item to the top of the stack           |
| peek()      | Return the top of the stack.                  |
| isEmpty ()  | Return true if and only if the stack is empty |


**使用情境:**

* 括號匹配
* 中綴表示法/後綴表示法
* Minimum Stack 
* DFS
* Recursive實作時


#### Monotone Stack
有兩種變化:
1. 比top小的值加入stack，比top大的值開始做處理 
2. 比top大的值加入stack，比top小的值開始做處理

**QP - stack 內的元素都是遞增或遞減**
    * [LeetCode Monotone stack](https://www.cnblogs.com/grandyang/p/8887985.html)  
    * [Monotone Questoin](Largest Rectangle in Histogram)


# Queue - First In First Out (FIFO)
| Function   | Description                                   |
| ---------- | --------------------------------------------- |
| remove()   | Remove the first item in the list.            |
| add(itern) | Add an item to the end of the list            |
| peek()     | Return the top of the stack.                  |
| isEmpty () | Return true if and only if the stack is empty |



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



# Leet Code 題目

| 題目                                                         | 描述                                                         | 解法                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **239. Sliding Window Maximum**                              | 給定一個組數以及窗口大小k, 返回該次窗口移動的最大值 <br>[1,3,-1,-3,5,3,6,7], 3. ->  [3,3,5,5,6,7] | 多種做法：<br>1. Nk : 每次移動窗口拾取最大值 <br/>2. multiset <br/>3. Max heap <br/>4. Deque (monotonic queue) |
| [341. Flatten Nested List Iterator](https://leetcode.com/explore/interview/card/top-interview-questions-hard/122/design/869/) | 實作一個iterator物件每次返回巢狀迴圈中的一個數字<br/>Input: nestedList = [[1,1],2,[1,1]] <br>Output: [1,1,2,1,1] |                                                              |



# Cracking Interview

| 題目             | 描述                                                         | 解法                                                         |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Three in One** | Describe how you could use a single array to implement three stacks | 1. 使用6個point去紀錄3個list的起始位子跟結束位子，當某個stack的資料沒地方放的時候要移動stack的位子<br>2. array中間隔去放3個stack的資料 |
| Stack Min        | How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time. | Min Max Stack                                                |
| Stack of Plates  | Imagine a (literal) stack of plates. If the stack gets too high, it might topple.<br/>Implement SetOfStacks composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack). <br/>FOLLOW UP<br/>Implement a function popAt(int index) which performs a popoperation on a specific sub-stack. | 有一個stack list，存放個個sub stack，如果stack滿了，則新增一個stack在list中，每次pop/push都先操最最新的stack |
| Queue via Stacks | Implement a MyQueue class which implements a queue using two stacks. | 使用兩個stack，第一個stack存資料，要remove時把第一個stack的資料再放到第個二個stack中，pop第二個stack的首原素 |
| **Sort Stack**   | Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. |                                                              |
| Animal Shelter   | An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure. | 使用兩個queue去做                                            |

