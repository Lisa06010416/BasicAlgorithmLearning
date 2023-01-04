# Linking List

* 新增刪除資料比較方便，但會需要比較多的儲存空間
* 主要是在考指針的修改 or 使用Linking List的結構減少複雜度

## 時間複雜度

|                               | linkling list | Array |
| ----------------------------- | ------------- | ----- |
| 查詢特定index資料             | O(n)          | O(1)  |
| 新增/刪除 資料                | O(n)          | O(n)  |
| 新增/刪除 資料 (已知節點位子) | O(1)          | O(n)  |



## 指針修改  merge/modify/insert

* reverse
* find mid/split link list - fast/slow point
    ```
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_head = slow.next
    ```

**技巧:**

* new head
* fast/slow point
    * 判斷是否有環
    * 找中點

**需要注意的地方:**
* 頭尾是否有空值的問題



## 使用 Linking List 的結構減少複雜度

* LRU Catch - Dict + Double Linking List



## Fast/Slow point | Runner Technique

### 找中點（或是任意等分點）

* 找中點 ：fast一次走兩格，slow走一格，當fast無法移動時，slow的下一個點會是中點（偶數的話會是把）linkling list評分的

  ​	```

  ```
  
            s       f   
  O -> O -> O -> O-> O
  
           s             f 
  O -> O-> O-> O -> O -> O
  ```

### Floyd’s Cycle Detection:

* 判斷是否有環 
  * 用快慢指徵如果有環的環兩個指針會相遇

* 找環的起點
  * 當快慢指針相遇後，把慢的指針放回head，兩個指針每次都只移動一格，相遇的點就是環的起始點

## Linking List with Recusive



## 題目

### 指針修改

| 題目           | 說明                                                         | 解法                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 146. LRU Cache | 實作一個LRU cache<br> least recently used (LRU)，把最久沒用的資料移出cache | 同時使用：double link link list來維護資料的順序以及hash(紀錄值以及node的映射)來查找資料，需要兩個操作：1. Get : 拿到特定值得node(用hash查找)，並更新node在list中的位子(把node移到list的head) <br>Put : 放入一個新的值，在dict內新增一個值以及node的映射，並把心node放到list的has，如果資料數量大於cache數，則刪除list尾端的node |



### 資料結構

| 題目              | 說明                                                         | 解法                                               |
| ----------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| 143. Reorder List | 將一個linkling list的後半部反轉叉戶前半部的node間，由 1->2->3->4 改為 1->4->2->3 | 先用快慢指針切分list，反轉第二個list在合併兩個list |



### Cracking Interview

| 題目                                                        | 說明                                                         | 解法                                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Remove Dups                                                 | Write code to remove duplicates from an unsorted linked list.<br/>FOLLOW UP : How would you solve this problem if a temporary buffer is not allowed? | 1. (需要額外空間)用dict計算出現過數字(O(n))<br>2. 先排序再刪除(O(nlogn)) <br>3. 雙層迴圈檢查(O(n^2)) |
| Return Kth to Last                                          | Implement an algorithm to find the kth to last element of a singly linked list. | 先遍歷一次整體長度，再去找第 N - K + 1 個node                |
| Delete Middle Node                                          | Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.<br>a->b->c->d->e->f   to   a->b->d->e- >f | 用快慢指針找中點                                             |
| Partition                                                   | Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.<br>Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] <br>Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 | 新增兩個smaller/bigger head 並遍歷linkling list，把值分別接到兩個head之後，最後再合併兩個list |
| Sum Lists                                                   | You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. | 分別遍歷兩個list，取得輸字並相加                             |
| Palindrome                                                  | Implement a function to check if a linked list is a palindrome. | 切分並reverse第二個list，在比較                              |
| Intersection                                                | Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value.That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting. | 判斷是否有環，快慢指針，Floyd’s Cycle Detection              |
| **Loop Detection**<br>160. Intersection of Two Linked Lists | Given a circular linked list, implement an algorithm that returns the node at the<br/>beginning of the loop. <br>Input: A -> B -> C -> D -> E -> C<br/>Output: C | 給一個環找出第一個開始重複的node，Floyd’s Cycle Detection    |

