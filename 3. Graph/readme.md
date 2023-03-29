# 3 Graph

[**Graph Theory**](http://publish.get.com.tw/bookpre_pdf/51MM045101-1.pdf)

| 名詞                   | 解釋                                                         | 作法                                                         |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| in-degree/out-degree   | 有像圖中某的點指入/出的邊樹                                  |                                                              |
| Span                   | 像樹一樣，每個點都連通但沒有cycle                            |                                                              |
| min span tree          | 每個邊上有weight，找到讓weight總和最小的邊的組合             | 把邊根據weight排序，由權重最小的邊開始判斷是否加入(edge_num = nodes_num - 1且不可以有cycle) |
| complete graph         | 任兩點間都有邊相連                                           |                                                              |
| Connected component    | 給予一個圖,彼此有通過相連的node為一個Connected component     |                                                              |
| Clique                 | 某個圖的子圖，且為 complete graph                            |                                                              |
| Directed Acyclic Graph | 有向無循環圖                                                 |                                                              |
| 樹, 森林, 圖的差別？   | 樹是指任意兩點之間都有且僅有一條路徑的無向圖。<br/>森林是指任意兩點之間至多僅有一條路徑的無向圖。<br/>由vertex和edge構成，可以分有像圖跟無相圖 |                                                              |



**Ｇraph 題目分析 ：**

| 問題                       | 答案                                                         |
| -------------------------- | ------------------------------------------------------------ |
| Graph 題目注意？           | 1. 圖是否有可能有不相連的情況2. 輸入的邊是否重複 <br>3. 無窮遞迴（走過的點是否會再被訪問） |
| 遍歷圖的方式？             | 1. BFS - 由queue中pop出一個點，將相鄰但還未拜訪的點放到queue中，並把當前的點標記為已拜訪<br/>2. DFS - 如果還有相鄰的點遞回拜訪<br/>3. **Bidirectional Search** : 找到兩個node中的最短path |
| 檢測圖中是否有環           | 1. edge_num >= nodes_num - 1 必有環<br>2. **Topology Sort** : 如果存在無法刪除的點(BFS)、重複拜訪的邊(DFS) -> 有環<br>3. DFS: 給每個點標記狀態 未訪問、訪問中、訪問結束，如果有連到訪問中的點代表有環 |
| Topology Sort是指什麼？    | 將DAG邊的指向作為依據排序                                    |
| Topology Sort 用DFS做法？  | <img src="readme.assets/截圖 2023-02-22 下午10.28.46.png" alt="截圖 2023-02-22 下午10.28.46" style="zoom:40%;" /> |
| Topology Sort 用ＢFS做法？ | <img src="readme.assets/截圖 2023-02-22 下午10.44.17.png" alt="截圖 2023-02-22 下午10.44.17" style="zoom:40%;" /> |



## 3.1 題目

##### 3.1.1 undirected graph

| Question                                                | Introduction                                             | Solution                                                     |
| ------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| 133. Clone Graph                                        | Clone Graph                                              | <img src="readme.assets/截圖 2023-02-21 下午8.21.41.png" alt="截圖 2023-02-21 下午8.21.41" style="zoom:50%;" /> |
| 261. Graph Valid Tree                                   | 判斷輸入的圖是否是樹                                     | tree 是一個 min span graph, node_num -1 = edge_num, 且由第一個node出發DFS/BFS找是否有連到全部的點 |
| **310. Minimum Height Trees**                           | 給予一張無向圖，找到用圖中的哪一點作為root可以讓樹高最小 | 作法1  是每一個點作為root DFS找樹高，找出樹高最小者<br/>作法2 這道題目其實是在考找圖的最中心的部分,作法類似BFS的Topological Ordering，紀錄每個點的連出去的edge數量，由最少的節點開始刪除，直到剩下兩個以下的點，這些點就是root |
| 323. number of Connected components in undirected graph | 找到輸入的圖中有多少的聯通的子圖(connect_component)      | 由一個未被拜訪的點出發，拜訪其所有可以連通的點，重複n次直到所有的點都被拜訪過，n就是連connected component |
| Route Between Nodes                                     | 給予一個有向圖以及兩個點，判斷兩點間是否有路             | **Bidirectional Search**<br>使用兩個queue: source queue 跟 dest queue，分別放入source跟des node初始化，量個交替做BFS，並且因為是有向圖所以要區分search的方向是forward或是backward |



##### 3.1.2 directed graph

| Question                | Introduction                                                 |                                                    |
| ----------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| 207. Course Schedule    | 給予一個課程順序清單 判斷該清單的順序是否是可行的 <br><img src="readme.assets/截圖 2023-02-22 下午10.56.34.png" alt="截圖 2023-02-22 下午10.56.34" style="zoom:50%;" /> | BFS/DFS topology sort，topology sort的結果是否有等於全部的node數 |
| 210. Course Schedule II | 給予一個課程順序清單 回傳可能的排課順序<img src="readme.assets/截圖 2023-02-22 下午10.55.48.png" alt="截圖 2023-02-22 下午10.55.48" style="zoom:50%;" /> | BFS/DFS topology sort   |
| 227. Find the celebrity | 在一個派對中有n個人，給予一個know(a,b)的函示回傳a是否認識b，找到n個人中的名人，名人的定義是一個人是所有人都認識但不認識其他人所有人 | 1. 使用雙層回圈去找任兩個人之間是否認識，並紀錄每個人人事跟被認識的數量，最後找出名人<br>2. (a)遍歷一次，找到celebrity candidate: 將一個人作為candidate，判斷candidate是否認識其他人knows(cand, i)，有的話將i作為新的candidate(b)在遍歷一次 確認 celebrity candidate 沒有認識任何人且任何人都認識他。 |
| 269. Alien Dictionary | 給予一個排序過的字典，但該字典不是按照一般的字元順序排序，找其字母間大小的關係<br>Input: [   "wrt",   "wrf",   "er",   "ett",   "rftt" ] <br>Output: "wertf" | 根據字母順序建立graph，像是由idx 0 可以知道 w > e > r，權重高的指向權重低的，在用topology sort 找到可行的排序 |
