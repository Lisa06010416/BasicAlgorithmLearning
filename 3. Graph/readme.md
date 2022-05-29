# Graph

* 樹是指任意兩點之間都有且僅有一條路徑的無向圖。
* 森林是指任意兩點之間至多僅有一條路徑的無向圖。

## Graph Theory
[Graph](http://publish.get.com.tw/bookpre_pdf/51MM045101-1.pdf)

| 名詞                | 解釋                                                     | 作法                                                         |
| ------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| in-degree/out-degree|有像圖中某的點指入/出的邊樹||
| Span                | 像樹一樣，每個點都連通但沒有cycle                        |                                                              |
| min span tree       | 每個邊上有weight，找到讓weight總和最小的邊的組合         | 把邊根據weight排序，由權重最小的邊開始判斷是否加入(edge_num = nodes_num - 1且不可以有cycle) |
| complete graph      | 任兩點間都有邊相連                                       |                                                              |
| Connected component | 給予一個圖,彼此有通過相連的node為一個Connected component |                                                              |
| Clique              | 某個圖的子圖，且為 complete graph                        |                                                              |



## 題目分析 ：

#### 注意 ：
1. 圖是否有可能有不相連的情況

2. 輸入的邊是否重複

3. 無窮遞迴（走過的點是否會再被訪問）

   

### 遍歷圖

* BFS

* DFS

* **Bidirectional Search** : 找到兩個node中的最短path
  
    * 交換由兩個點做BFS
    
      

### 檢測圖中是否有環

tips:

* edge_num >= nodes_num - 1 必有環


**Topology Sort** :

    * 如果存在無法刪除的點(BFS)、重複拜訪的邊(DFS) -> 有環
    
**DFS**:

    * 給每個點標記狀態 未訪問、以訪問中、訪問結束
    * 如果有連到訪問過的點代表有環
    
      

### :star::star::star:[拓樸排序](http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html)

常用來來找是否存在合理順序

* DFS Topology Sort - 離開點的順序反過來會是Topological Order(離開順序 2,1,0，Topological Order 0,2,1)

    ```
    
    adj = [[1,0,1], 
           [0,1,0], 
           [1,0,1]]
    visit = [0, 0, 0]
    is_cycle = False
    topoloｇy_order = []
    
    
    def dfs(i):
    	  if (visit[i] >= 1):  # 如果重複拜訪代表有環
    		    cycle = True
    		    return None
    	
    	  visit[i] = 1    # 記錄該點走過
    	  for  j in range(0, len(adj)):  ＃ 如果該點有連接到的點，繼續dfs
            if adj[i][j]: 
                DFS(j);
        topolody_order.append(i)  # 將該點加入 topoloｇy_order
    
    for i in range(0, len(adj)):  # 對還沒有拜訪過的點做dfs找topoloｇy_order
        if not visit[i]:
           dfs(i)
           
    if (cycle)
        print("has cycle!!")
    else
       # 離開點的順序，頭尾顛倒之後，就是拓撲順序。
       print(topoloｇy_order[::-1])
    ```
    
* BFS  Topology Sort - 不斷的找入度為0的點(點0 -> 1 -> 2)刪除以及相連的邊，被刪除的加入Topological Ordering中

    ```
    adj = [[1,0,1], 
           [0,1,0], 
           [1,0,1]]
    edge_count = [0,0,0]
    topoloｇy_order = []
    
    def bfs():
        # 記錄圖上每一個點目前仍被多少條邊連到
        for i in range(len(adj)):
            for j in range(len(adj)):
                 if i != j and adj[i][j]:
                     edge_count[j] += 1
        
        # 尋找沒有被任何邊連向的點
        for i in range(len(edge_count)):  # 每次pop一個點要 pop edge_count 次
            # 找到一個沒有被連到的點
            s = 0
            while ref[s] != 0:
                s += 1
                if (s == 9)： # 找不到 -> 有環
                    return None
            ref[s] = -1
            topoloｇy_order.append(s)
            if edge_count == 0:
                edge_count
        
           # 更新ref的值（刪去由s點連出去的邊）
           for t in range(len(edge_count)):
                if adj[s][t]:
                    ref[t] -= 1
       return topoloｇy_order
             
    
    ```
    
    
    
* 題目類型 ：
    * 是否有合理的拓樸排序
        -[ ] 207. Course Schedule
    * 列出全部可能的排序 - backtracking
    * 可能排序的個數
        -[ ] ZOJ 1346 Comparing Your Heroes
    * BFS可以用來找DAG中最中心的部分
        -[ ] 310. Minimum Height Trees

## 題目

##### undirected graoh

| Question                                                | Introduction                                             | Solution                                                     |
| ------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| 133. Clone Graph                                        | Clone Graph                                              | DFS/BFS 遍歷圖                                               |
| 261. Graph Valid Tree                                   | 判斷輸入的圖是否是樹                                     | tree 是一個 min span graph, node_num -1 = edge_num, 且由第一個node出發DFS/BFS找是否有連到全部的點 |
| **310. Minimum Height Trees**                           | 給予一張無向圖，找到用圖中的哪一點作為root可以讓樹高最小 | 作法1  是每一個點作為root DFS找樹高，找出樹高最小者<br/>作法2 這道題目其實是在考找圖的最中心的部分,用BFS的Topological Ordering，由最外圍的節點開始刪除，直到剩下兩個以下的點，這些點就是root |
| 323. number of Connected components in undirected graph | 找到輸入的圖中有多少的聯通的子圖(connect_component)      | 由一個未被拜訪的點出發，拜訪其所有可以連通的點，重複n次直到所有的點都被拜訪過，n就是連connected component                                                |



##### directed graph

| Question                | Introduction                                                 |                                                    |
| ----------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| 207. Course Schedule    | 給予一個課程順序清單 判斷該清單的順序是否是可行的 <br>2, [[1,0]]  => True <br>2, [[1,0],[0,1]] => False (克會相衝) | topology sort  判斷有向圖是否有環 （有環的話會在還有node沒有被sort的情況下找不到可以刪除的candidate) |
| **210. Course Schedule II** | 給予一個課程順序清單 回傳可能的排課順序 | topology sort 回傳一個可能的 topology sort 的結果                        |
| 227. Find the celebrity | 給予一個know(a,b)的函示回傳a是否認識b，找到n個人中哪一個人是所有人都認識但不認識其他人的人 | 遍歷一次，找到celebrity candidate: 將啲一個人作為candidate，判斷candidate是否認識其他人knows(cand, i)，有的話將i作為新的candidate，在遍歷一次 確認 celebrity candidate 沒有認識任何人且任何人都認識他。 |
| 269. Alien Dictionary | 給予一個排序過的字典，找地其字母間大小個關係<br>Input: [   "wrt",   "wrf",   "er",   "ett",   "rftt" ] <br>Output: "wertf" | 根據字母順序建立direct graph，權重低的紙箱權重高的，在用topology sort 找到可行的排序 |



##### Cracking Interview

| Question                | Introduction                                                 |                                                    |
| ----------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
|Route Between Nodes| 給予一個有向圖以及兩個點，判斷兩點間是否有路 | **Bidirectional Search** |
|Build Order| 給予projects間的優先順序，找到一個合理的順序<br>Input: projects: a, b, c, d, e, fdependencies: (a, d), (f, b), (b, d), (f, a), (d, c) <br/>Output: f, e, a, b, d, c |Topology Sort|