# Graph

* in-degree 入度
* our-degree 出度
* 樹是指任意兩點之間都有且僅有一條路徑的無向圖。
* 森林是指任意兩點之間至多僅有一條路徑的無向圖。

## Graph Theory
[Graph](http://publish.get.com.tw/bookpre_pdf/51MM045101-1.pdf)
* min span graph
* complete graph - 任兩點間都有邊相連
* Clique - 某個圖的子圖，且為 complete graph
* Connected component - 給予一個圖,彼此相連的子圖為一個Connected component


## 題目分析 ：
#### 考慮問題 ：
1. 圖是否有可能有不相連的情況
2. 輸入的邊是否重複
3. 無窮遞迴


#### 題目類型 : 

基本上是遍歷圖，再加上各種判斷，跟tree比較起來，比較常需要使用 hashmap 記錄節點


* 檢測圖中是否有環
    * tips :
        * 如果兩點間不會有重複邊則: edge_num >= nodes_num - 1 必有環
        * 快慢指針
        
* min span tree
    * 在 edge_num = nodes_num - 1 的情況下, 遍歷看看是否有經過全部的點
    * Tree or graph :
        * Tree 會是一個 min span graph , node_num -1 = graph_num , 且可以連通道每一個點
    

* Direct Graph
    * Directed Acyclic Graph(DAG)
        * 排序問題，某點要在某點之前
        * [拓樸排序](http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html)
        * 作法： 0 -> 1 -> 2
            * DFS - 離開點的順序反過來會是Topological Order(離開順序 2,1,0，Topological Order 0,2,1)
            * BFS - 不斷的找入度為0的點(點0 -> 1 -> 2)刪除以及相連的邊，被刪除的加入Topological Ordering中
        * 題目類型 ：
            * 是否有合理的拓樸排序
                -[ ] 207. Course Schedule
            * 列出全部可能的排序 - backtracking
            * 可能排序的個數
                -[ ] ZOJ 1346 Comparing Your Heroes
            * BFS可以用來找DAG中最中心的部分
                -[ ] 310. Minimum Height Trees
