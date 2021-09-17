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
    *  題目有類似任意節點...所有節點...
    
## 常見的tree
* prefix tree - 字典查詢字
* Expression Tree
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
