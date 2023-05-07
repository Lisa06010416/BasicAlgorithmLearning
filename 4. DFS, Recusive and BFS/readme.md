

# 4 BFS and DFS



| 問題                 | 題目                                                         |
| -------------------- | ------------------------------------------------------------ |
| BFS 常用的２個地方？ | 1. 常用於找最短路徑（找最短路徑可以考慮用bidirect search）<br>2. BFS 可以忽略不佳的解，找到答案便會停止(可以忽略會來回走的陷阱) |
| ＤFS 常用的方法？    | 1, 通常題目有"找到全部的..."<br>2. 可以看是否要使用 recursive + memory = dp 減少判斷的過程<br/>3. 注意寫程式的時候使用的記憶體跟時間(<br>   a. 像是如果傳入一個被修改的陣列或自傳需要Ｏ(n)，但傳indx只要Ｏ(1)<br>   b. 可以盡量共用物件減少空間的使用 |
| DFS的時間複雜度？    | 可以畫樹來計算，並使用menory減少時間複雜度                   |
| 需要注意的？         | 1. 結束的條件 <br>2. 往下遞回的過程(特別是開始跟結束)<br>3. 是否可以用cache 或 memory 加速<br>4. **使用 @cache function的參數不能有不能hash的物件** ex lisa |

# 4.1 題目

## 4.1.1 BFS/DFS/BackTracing

| 問題                                          | 描述                                                         | 解法                                                         |
| --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 37. Sudoku Solver                             | 給一個board，完成數獨遊戲<br><img src="readme.assets/截圖 2023-02-28 下午4.42.09.png" alt="截圖 2023-02-28 下午4.42.09" style="zoom:30%;" /> | backtracing，用DFS找全部的可能<br>如果某個空格沒有數字，則找到可以填的數字(行列中沒有重複的數字）填入grid後再呼叫dfs去填下一個數字 |
| 22. Generate Parentheses                      | 給予一個數字n代表要生成幾個括號pair的字串，回傳所有可能的結果<br>Input: n = 3 <br/>Output: ["((()))","(()())","(())()","()(())","()()()"] | DFS，遞迴生成全部括號字串，紀錄當下已經生成的左右括號數量，如果左括號數量小於n則可以生成左括號，又括號樹小於左括號則可以生成又括號 |
| 39. Combination Sum <br>40. Combination Sum 2 | 給予一個canditates的數列，以及target，求任意選canditates中數字的和可以等於target的全部可能<br>39: canditates中每個數字可以用無限次<br>40: canditates中每個數字只可以用一次，且canditates中會有重複的數字 | 基本上都適用dfs求全部的解，差在重複判斷的部分，跟46題的重複判斷比較的差別是這裡在遍歷的時候只需要判斷後面的元素，因此不需要額外使用visited判斷前面的元素是否被使用<br><img src="readme.assets/截圖 2023-03-01 下午9.58.34.png" alt="截圖 2023-03-01 下午9.58.34" style="zoom:150%;" /> |
| 46. Permutations<br>47. Permutations II       | 兩題差別在輸入數字是否會重複，給予一個數列nums，回傳該數列全部的組合<br>Input: nums = [1,2,3]<br/> Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] | DFS找到全部的結果，如果要避免重複：<br>1. 使用set或是hash紀錄結果<br>2. 在遞回的過程中避免重複：紀錄每個數值的visited，第n個重複的數字只有當visited=n-1時才可以使用<br><img src="readme.assets/截圖 2023-02-28 下午7.58.55.png" alt="截圖 2023-02-28 下午7.58.55" style="zoom:50%;" /> |
| 31. Next Permutation                          | A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.<br>For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.<br>The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).<br>Input: nums = [1,2,3] Output: [1,3,2] | <img src="readme.assets/截圖 2023-05-07 下午7.38.38.png" alt="截圖 2023-05-07 下午7.38.38" style="zoom:150%;" /> |
| 127. Word Ladder                              | 給予 beginword, endword 以及一串字串，每次可以替換beginword的一個字元， 找出最少要幾個詞梯才可以達到endword<br/><img src="readme.assets/截圖 2023-02-22 下午11.46.54.png" alt="截圖 2023-02-22 下午11.46.54" style="zoom:50%;" /> | 1. BFS，相當於油beginword開始每個字元可以有26個可以走的路徑，找除beginword道endword的最短路徑<br><img src="readme.assets/截圖 2023-02-28 下午3.14.03.png" alt="截圖 2023-02-28 下午3.14.03" style="zoom:150%;" /> |
| 301. Remove Invalid Parentheses               | 給予一個帶括號的字串，找除移除最少括號使其合法的全部可能<br><img src="readme.assets/截圖 2023-02-22 下午11.48.21.png" alt="截圖 2023-02-22 下午11.48.21" style="zoom:50%;" /> | 1. BFS，將input s作為BFS２的起點，如果該點isvalid(如果左右括號數相等，且每個又括號左邊一定要有左括號)，則回傳，如果不合法則遍歷去除一個括號，如國新的s之前沒有拜訪過，加入queue中<br>2. DFS，計算多餘的左又括號數量，每次遞迴時根據多餘的左右括號數回圈看是否要刪掉括號，如果有多個連續的左or右括號，刪除其一即可<img src="readme.assets/截圖 2023-02-28 下午3.52.07.png" alt="截圖 2023-02-28 下午3.52.07" style="zoom: 150%;" /> |
| 464. Can I Win                                | 兩個玩家輪流選數字(不可以重複)，直到某次數字大於限制時則該玩家輸掉遊戲，給予兩個餐參數，maxChoosableInteger＝n代表可以在1-n中選數字，desiredTotal=m 代表當兩個玩家選的數字和大於m時該玩家輸掉遊戲，寫一個程式判斷遊戲的結果，回傳true表示第一個玩家一定可以贏否則回傳False<br><img src="readme.assets/截圖 2023-03-01 下午11.09.10.png" alt="截圖 2023-03-01 下午11.09.10" style="zoom:150%;" /> | <img src="readme.assets/截圖 2023-03-01 下午11.02.48.png" alt="截圖 2023-03-01 下午11.02.48" style="zoom:150%;" /> |

