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
