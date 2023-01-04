# Recusive
* 畫樹來計算相似度

# DFS 
 
 
# BFS
* 某些題目可能可以用BFS（只要找最短路徑時）, 空間複雜度會比較好, ex
    * Finding a shortest path in a nxm matrix

* BFS 可以忽略不佳的解，找到答案便會停止(可以忽略抹些會來回走的陷阱)
    有迷宮出發
    
| 問題                          | 描述                                                         | 解法                                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
|127. Word Ladder | 給予 startword, endword 以及一串字串 找出最少要幾個詞梯才可以達到endword| BFS (只要找最短路徑）




# Backtracking

* 通常題目有"找到全部的..."

* recursive + memory = dp

* [State Compression dp](https://mp.weixin.qq.com/s?__biz=MzI4MzUxNjI3OA==&mid=2247486874&idx=1&sn=0f27ddd51ad5b92ef0ddcc4fb19a3f5e&chksm=eb88c183dcff4895209c4dc4d005e3bb143cc852805594b407dbf3f4718c60261f09c2849f70&token=1227596150&lang=zh_CN#rd): 用bit操作來紀錄狀態

* 注意 可以使用同一個物件節省記憶體
    * Palindrome Partitioning
    
    
| 問題                          | 描述                                                         | 解法                                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
|127. Word Ladder | 給予 startword, endword 以及一串字串 找出最少要幾個詞梯才可以達到endword| BFS (只要找最短路徑）
|212. Word Search  II| 給予一個board以及一組word list，找出有多少字出現在board中|backtracting+tri|
|301. Remove Invalid Parentheses|給予一個帶括號的字串，找除移除最少括號使自傳合法的全部可能||

### 注意list的memory
* copy and deep copy
* list
  * 新的物件
  ```
    a_list = []  # 傳值
    a_list = a_list[0:3] 
  ```
    
