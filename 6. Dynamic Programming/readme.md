# Dynamic Programming
* [DP Pattern](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)

* DP 本身和 memory + recursive 十分相似，只是遍歷值的方法不同

* DP
    * 特性 :
        * 可以將一個問題分成子問題，當子問題有最佳解時，組合起來也會是最佳解
    * 步驟 :
        * 定義dp函式
        * 轉移方程式
        * 確定初始化方式
    
    
* 題目類型
    * 背包問題
        * 參考資料 
            * [背包問題九講](http://www2.lssh.tp.edu.tw/~hlf/class-1/lang-c/DP.pdf)
        * 題型：
            * 0/1背包問題 (01 knapsack problem)
            * 完全背包問題 (unbounded knapsack problem)
            * 多重背包問題 (bounded knapsack problem)
            * 是否要裝滿 - 初始化方式
    * range dp:
        * dp[j] - 代表一個區間內的數值
        * dp[i][j] - 代表區間i-j內的數值
        
* 計算編輯距離