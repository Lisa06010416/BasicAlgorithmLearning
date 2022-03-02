# Tree

## 題型 ：

* 搜索/遍歷/序列化 ：
  * 搜索方法分類 : 
    * BFS - Use Queue
    * DFS - Recursive/For Loop(use stack)
      * InOrder, Preorder, Postorder

* 建構（反序列化）：

    * 給便利順序建構樹,  根據 Inorder 確定root，根據 Postorder/Preorder 切分左右子樹（BST不需要）

* 修改 - 增加刪除節點

## 技巧：

* Full binary tree
    * serialization
    * deserialization
    
* 雙層 Recusive
    * 題目有類似任意節點...所有節點...
    
      
    
## 常見的tree
### Binary Search Tree

1. 定義：左 < 中 < 右，且不存在相等的節點

2. In-order traversal的結果會是有序的

3. 常用操作：查詢、插入、刪除

    | 演算法 | 平均時間複雜度（balance） | 最差時間複雜度（skew） |
    | ------ | ------------------------- | ---------------------- |
    | 搜尋   | Log n                     | n                      |
    | 插入   | Log n                     | n                      |
    | 刪除   | Log n                     | n                      |

    * **查詢**

      * 查詢target

      * 找到ＢＳＴ中小於/小於等於target的最大值node

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
            return result
        ```

      * 找到ＢＳＴ中大於/大於等於target的最小值node

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

    * **刪除**

      * 該節點沒有左右子樹  -> 直接刪除
      * 該節點只有右子樹     ->  刪掉節點，將右子樹替換到刪除節點的位子
      * 該節點只有左子樹    ->  找到刪除節點左子數中的最大值的節點替換到刪除節點的位子
      * 該節點有左右子樹    ->  找到刪除節點左子數中的最大值的節點替換到刪除節點的位子

    * **插入**

      * 不斷做search直到空節點，在該位置新增節點



#### BST 題目

| 題目                                    | 題目說明                                                     | 解法                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LeetCode 285 : Inorder Successor in BST | 給予一個BST以及樹中的一個node找到該node的in-order traversal的successor | 1. 忽視ＢＳＴ特性，直接用中序遍歷去找target node的successor Binary Search Tree <br/>2. 使用ＢＳＴ特性，In-order traversal會是按照排序過的順序的，找樹中最接近且大於target的node |
| Pramp : Largest Smaller BST Key | 給予一個BST以及樹中的一個node找到該樹中小於target node的最大node | 找到ＢＳＴ中小於target的最大值node |
|                                         |                                                              |                                                              |
|                                         |                                                              |                                                              |
|                                         |                                                              |                                                              |

### Prefix Tree

* 字典查詢字

### Expression Tree
   * operator priority:
     
   * 題目：

    - [ ] 367 Expression Tree Build
        * ascending stack + tree
    - [ ] 368 Expression Evaluation (見stack)
        * 不同表達式計算：
            * Inorder - 很麻煩 [inorder](https://medium.com/@xingren14/368-expression-evaluation-f8c4270ec27)
            * postorder  - 可以忽略括號，由**左而右**掃描，當事數字時入stack，符號時pop，處理完再將新的數字入stack
            * preorder  - 可以忽略括號，由**右而左**掃描，當事數字時入stack，符號時pop，處理完再將新的數字入stack
        * 作法 :
            * stack + postorder
            * build expresion tree and traversal
    - [ ] Build Binary Expression Tree From Infix Expression
