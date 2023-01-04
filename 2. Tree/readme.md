# Tree
## 定義
* 一定會有root
* 每個node會有 0-n 個 child
* 不會有cycle，每個node都會相連
  * **edge num = node num - 1**
* 樹也是一種graph

## 常用術語

| 樹                  | 說明                                                         |
| ------------------- | ------------------------------------------------------------ |
| Balance             | 任一個節點左右子樹的高的差<=1                                |
| complete            | 除了最後一層以外，每一層的會被填滿，且最後一層會按左到右填滿 |
| Full Binary Tree    | 每一個node都有兩個子node                                     |
| Perfect Binary Tree | complete 且 Full，每一層的會被填滿                           |

## 題型：

* 搜索/遍歷/序列化 ：
  * 搜索方法分類 : 
    * BFS - Use Queue
    * DFS - Recursive/For Loop(use stack)
      * InOrder, Preorder, Postorder

* 建構（反序列化）：

    * 給便利順序建構樹,  根據 Inorder 確定root，根據 Postorder/Preorder 切分左右子樹（BST不需要）

* 修改 - 增加刪除節點

## 技巧：

* 使用 Full binary tree 的結構來幫忙做：
    * serialization
    * deserialization
    
* 雙層 Recusive ：
    * 題目有類似任意節點...所有節點...
    
## 題目
### Tree 遍歷/搜尋/序列化

| 問題                          | 描述                                                         | 解法                                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
|94 Binary Tree Inorder Traversal|回傳一棵樹的inorder順序|序列化，用BFS/Stack|
|98. Validate Binary Search Tree|驗證一棵樹是不是BST|BST規則，遍歷tree|
|100. Same Tree|給予兩棵樹的root判斷兩棵樹是否一樣|遍歷tree|
|102. Binary Tree Level Order Traversal|將一顆ＢＳＴ轉為Level Order sequence|BFS|
|104. Maximum Depth of Binary Tree|球衣客數最大深度|遍歷樹 or 序列化判斷|
|**124. Binary Tree Maximum Path Sum**|找到一顆樹中有個leaf node組成的path的最大值|DFS，每個root找齊左右節點的最大值，加上自己後判斷是要更新答案|
|226. Invert Binary Tree|反轉一個二元樹(左子樹變右子樹)|DFS，離開node時交還左右子樹|
|**235. Lowest Common Ancestor of a Binary Search Tree**|給一棵BST，找出樹上兩個點的最低共同父節點LCA(lowest common ancestor)|用ＢＳＴ加快查尋|
|236. Lowest Common Ancestor of a Binary Tree|給一棵樹，找出樹上兩個點的最低共同父節點LCA(lowest common ancestor)| 需要由子節點回傳判斷資訊 |
|572. Subtree of Another Tree|判斷一棵樹是否是賃一棵樹的substree|遍歷第一課樹找到每個subtree，跟第二棵樹比較|

### construct tree
| 問題                          | 描述                                                         | 解法                                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
|                                                              |                             |                                       |
|**105. Construct Binary Tree from Preorder and Inorder Traversal**|透過preorder、inorder建立BT|preorder確認root，inorder確認左右子樹|



## 常見的tree

### Binary Tree
* 每個node至多只有兩個child



### Binary Search Tree :star::star::star::star::star:

1. 定義：左 < 中 < 右(**In-order traversal的結果會是有序的**)，且**不存在相等的節點**

3. BST 常用操作：

    | 演算法 | 平均時間複雜度（balance） | 最差時間複雜度（skew） |
    | ------ | ------------------------- | ---------------------- |
    | 搜尋   | Log n                     | n                      |
    | 插入   | Log n                     | n                      |
    | 刪除   | Log n                     | n                      |

    * **查詢**

      * 查詢target

      * **找到ＢＳＴ中小於/小於等於target的最大值node** 

        ```
        function findLargestSmallerKey(rootNode, target):
            result = -1
            while (rootNode != null):
                # 往右表示目前的node<target (target在右邊)，目前的node小於target淺在解答，更新result
                if (rootNode.key < target): # rootNode.key <= target => 小於等於target的最大值node
                    result = rootNode.key
                    rootNode = rootNode.right
                # 往左表示目前的node>target(target在左邊)，目前的node不會是淺在的答案
                else: 
                    rootNode = rootNode.left
            return resul
        ```

      * **找到ＢＳＴ中大於/大於等於target的最小值node**

        ```
        function findLargestSmallerKey(rootNode, target):
            result = -1
            while (rootNode != null): 
                # 往左表示目前的node>target(target在左邊)，目前的node大於target可能為答案，更新result
                if (rootNode.key < target):  # rootNode.key <= target => 大於等於target的最小值node
                	result = rootNode.key
                	rootNode = rootNode.left
                else: # 往右表示目前的node<target (target在右邊)，目前的node小於target不可能為答案
                  rootNode = rootNode.right
            return result
        ```

    * :star:BST**刪除**

      * 該節點沒有左右子樹  -> 直接刪除
      * 該節點只有右子樹     ->  刪掉節點，將右子樹替換到刪除節點的位子
      * 該節點只有左子樹    ->  找到刪除節點左子數中的最大值的節點替換到刪除節點的位子
      * 該節點有左右子樹    ->  找到刪除節點左子數中的最大值的節點替換到刪除節點的位子

    * BST**插入**

      * 不斷做search直到空節點，在該位置新增節點

#### BST 題目

| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| :star:**LeetCode 285 : Inorder Successor in BST** | 給予一個BST以及樹中的一個node找到該node的in-order traversal的successor | 1. 忽視ＢＳＴ特性，直接用中序遍歷去找target node的successor Binary Search Tree <br/>2. 使用ＢＳＴ特性，In-order traversal會是按照排序過的順序的，找樹中最接近且大於target的node |
| **Pramp : Largest Smaller BST Key** | 給予一個BST以及樹中的一個node找到該樹中小於target node的最大node | 找到ＢＳＴ中小於target的最大值node |
| **230. Kth Smallest Element in a BST** | 找到ＢＳＴ中第k個小的值  | 中序遍歷到第Ｋ個值                                                               |
| **Minimal Tree**<br>108. Convert Sorted Array to Binary Search Tree | 給予一個排序好且元素不重複的array，設計一個方法可以建出樹高最小的BST | 遞迴切分array，每一次都丟中間的值去建立BST，左右再分別遞迴   |
| :star:**BST Sequences**                                      | 給予一顆ＢＳＴ，回傳可能可以建出該樹的全部input array        | 不斷移除一個root,將其子樹的root加入candidate set中，遞迴求全部的解 |
| **95. Unique Binary Search Trees II**                        | give a postive number n, generate all BST which has node id from 1 to n | backtracking(每個node分別視為root)，切分做又序列，使用memory紀錄在序列i-j可能有的root，如果該區間已經計算國則直接使用之前計算的結果 |



### Binary Heap / Min/Xax Heap / Priority Queue  :star::star::star:

* 是一個**complete binary tree**

* priority queue的一種實作方法

* 常用於：對一個**變動的**數列找**最大/最小/第Ｋ個大or小的數**

* Heap implement （min heap）

  |                | **Average**                                                  | **Worst case** |
  | -------------- | ------------------------------------------------------------ | -------------- |
  | **Space**      | O(n)                                                         | O(n)           |
  | **Search**     | O(n)                                                         | O(n)           |
  | **Insert**     | **O(1)** <br/>For a random insert sequence: 1/2\*1 + 1/4 \* 2 + ... | O(log n)       |
  | **Find-min**   | O(1)                                                         | O(1)           |
  | **Delete-min** | O(log n)                                                     | O(log n)       |

  * Pop root （down heap)
    1. 將root node的值拿出來
    2. 將complete tree的最後一個node放到root的位子
    3. 不斷比較新的root以及其子節點，如果新root的值比子節點大則交換兩個node的位子（如果比兩個子節點都大則跟最小的換），直到順序正確
  * push (up-heap)
    * 將新node插入到樹中的最後一個位子，如果該node比其父node小則交換兩個node，直到順序正確
  * push then Pop - 會比先 Insert 在 Pop 還要快
    * 比較新增的node以及現有的root哪個表較小，將比較小的作為新的root
    * 對新的root做down heap
  * Heapify
    * 由**最後**一個節點開始檢查每一個節點是否符合規則，不符合則調整順序(down heap)

* heap sort

  1. 將一個array建成heap
  2. 不斷地將heap中的值pop出來
  
* heap Python 套件

  ```
  import heapq
  heap_list = [1, 2, 3]
  ＃heapify
  heapq.heapify(heap_list) ＃min heap, max heap 數值加負號
  ＃放入值
  heapq.heappush(heap_list, nums)
  # 取出值
  heapq.heappop(heap_list)
  # 放入後取出一個值
  heapq.heappushpop(heap_list, nums)
  ```

* Heap 題目：

| 題目                                             | 描述                                                         | 解法                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **23. Merge k Sorted Lists**                     | 給予k個排序好的link list，將他們merge成一個                  | Heap                                                         |
| 239. Sliding Window Maximum                      | 給定一個組數以及窗口大小k, 返回給次窗口移動的最大值 <br>[1,3,-1,-3,5,3,6,7], 3. ->  [3,3,5,5,6,7] | 多種做法：<br>1. Nk : 每次移動窗口拾取最大值 <br/>2. multiset <br/>3. Max heap <br/>4. Deque (monotonic queue) |
| **295. Find Median from Data Stream**            | 求一個可變數列的median                                       | 同時使用min/max heap，min heap放最大的前一半的數列，max heap放剩下較小的數列，每次插入值的時候判斷新的值要放在哪一個heap中，並平衡兩個heap的長度，由兩個heap的root計算median |
| **313. Super Ugly Number**                       | 給予一個質數列表找到地n個Super Ugly Number(是指其全部的prime factor都在給定的prime list中) | min heap primes = [2,3,5] <br/> (2)  *2, 2^2, *2^2, 2^3 <br/>(3)   3,  *3,  3^2, 3^2 <br/>(5)   4,   4,   *4, 4^2 <br/>urgly_number_sep = [1, 2, 3, 4, 6]<br/>可以看到每次要選的都是3者中的最小值(有*者)，把最小值由min heap中pop出來（一樣的值要全部一起拿出來），在將下一個數值放入，重複n次 |
| 347. Top K Frequent Elements                     | 給一個nums array找出前k個最常出現的數字，時間複雜度小於 O(n log n) <br>Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2] | 計算每一個數字的出現次數並加入heap，再由heap中pop出k個數值   |
| **378. Kth Smallest Element in a Sorted Matrix** | 給予一個行與列都排序好的matrix，找到地k個小的元素<br/>Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 Output: 13 | 1. 把數值加入max heap中，如果heap內的值大數量於k，則pop，最後root會是答案<br>2. **binary search** |
| 218. The Skyline Problem                         | [說明](https://leetcode.com/problems/the-skyline-problem/)，給予一組建築物的list(start, end, hight)，計算出skyline<br>Input: buildings = [[0,2,3],[2,5,3]] <br>Output: [[0,3],[5,0]] | 用heap動態確認每個點的最大值                                 |



### Prefix Tree / Trie

* 用於建立字典，查詢字

#### 題目
| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|208. Implement Trie (Prefix Tree)|實作prefix tree||
|211. Design Add and Search Words Data Structure| 建立一顆prefix tree，查詢時可以有.替代全部的字元|DFS 遇到.則全部的子節點都查詢|
|212. Word Search II|給予一個字母board,跟一串word,回傳有哪些word在board中|將words建成prefix tree，並遍歷board將每個chr作為起點，由四個方向DFS的去找是否有符合的word，時間複查度Ｏ(4^max(word_len))|



### Expression Tree

   * 切扯到 expression 多要用 **stack**，或是**monotonic stack**
   * 題目：
        * Expression Tree Build : ascending stack + tree
        * Expression Evaluation:
        * Inorder - 772. Basic Calculator III
        * postorder  - 可以忽略括號，由**左而右**掃描，當是數字時入stack，符號時pop，處理完再將新的數字入stack
        * preorder  - 可以忽略括號，由**右而左**掃描，當是數字時入stack，符號時pop，處理完再將新的數字入stack

#### 題目
##### expression tree
| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|LintCode 367 · Expression Tree Build|將一個算式變為Expression Tree|monotonic stack|

##### expression calculator
| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|227. Basic Calculator II|給一個有可能有＋-*/的計算式，取得答案|第一次遍歷計算式，將數字放到stack中，遇到-則對數字加上負號，遇到＊/則pop出一個數字跟符號後的數字做計算，再把結果放到stack，第一次遍歷結束代表＊/都已完成將stack內的結果sum起來就是答案 |
|772. Basic Calculator III|比Basic Calculator II多了括號的部分|碰到括號後把括號的部份丟入遞迴計算答案|



### AVL Tree

* 目的是讓ＢＳＴ不要過度傾斜
* 對每個節點判斷是否傾斜（左子樹高與右子樹高差過1)，傾斜則對樹做旋轉



### Red Black Tree

* 目的是讓ＢＳＴ不要過度傾斜

* 最長路徑不會超過最短path的兩倍

  

## Cracking Interview - Tree

| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Check Balance         | 確認一顆ＢＴ是否是balance                                    | 遞迴檢查每個node的左右子樹的差是否<=1                        |
| Valid BST             | 確認一顆ＢＴ是否是ＢＳＴ                                     | 檢查每一個node是否 左<中<右                                  |
| :star:**Random Node** | You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods | 1. 把樹轉乘inorder的形式，random回傳一個node <br/>2. 改變樹的結構，每個node多紀錄現在是第幾層，random選層數(層數的權重跟node樹一樣)以及每次要往左或往右 |
| Implement BST         | Implement find, insert, **delete**                           |                                                              |





