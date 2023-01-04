# Array and String

* 如果只是要記錄字元有/沒有（兩種狀況以內），可以用bit替代array減少時間複雜度



## Python string 操作

* 如何將一個字串的字元排序

  ````
  可以直接對 str sorted,會變成sorted list ：
  sorted('rea') # ['a', 'e', 'r']
  ````
  
* string不能直接指定值

  ```
  (X) 
  s[4] = 'a'
  
  (O)
  char_list = [char for char in s]
  char_list[4] = 'a'
  ```

* re套件

  * Function
  
    | Funciton                                        | Intro                                  |      |
    | ----------------------------------------------- | -------------------------------------- | ---- |
    | re.match(pattern, string, flags)                | 指匹配由開頭開始的（匹配一次）         |      |
    | re.search(pattern, string, flags)               | 匹配整個字符串（匹配一次）             |      |
    | findall(pattern, string, pos, endpos)           | 匹配所有符合規則的字符，反回符合的字串 |      |
    | re.sub(pattern, repl, string, count = 0, flags) | 替換                                   |      |
    | re.split(pattern, string, maxsplit, flags)      | 切分，用（）可以保留切分的字符         |      |
  
    * match/search result: group and span
  
      ```
      string = "hello 123abc"
      r = re.search("1(2)(3.*)", string)
      
      # 查看結果index與匹配的字串
      print(r)
      print(r.span())    # (6, 12)
      print(r.group())   # 123abc
      print(r.group(1))  # 2
      print(r.groups())  # ('2', '3abc')       
      ```
  
      
  
  * Re-Regilar Expression
  
    | 符號  | 說明          | 符號 | 說明                   | 符號   | 說明             |
    | ----- | ------------- | ---- | ---------------------- | ------ | ---------------- |
    | .     | 任何字符      | \d   | 數字                   | [...]  | 裡面任一個符號   |
    | *     | 出現0次或多次 | \D   | 非數字                 | [^...] | 非裡面任一個符號 |
    | +     | 出現一次以上  | \s   | 空白字符               | ()     | 分組             |
    | ?     | 0次或1次      | \S   | 非空白字符             | ｜     | 或               |
    | {n,m} | 出現m-m次     | \w   | 大小寫英文字母、數字   | ^      | 字符串的起點     |
    |       |               | \W   | 非大小寫英文字母、數字 | $      | 字符串的結尾     |
  
    
  
* Char Order

  ```
  ord('0') <-> chr(48)
  ord('9') <-> chr(57)
  
  ord('A') <-> chr(65)
  ord('Z') <-> chr(90)
  
  ord('a') <-> chr(97)
  ord('z') <-> chr(122)
  ```

* String build-in

  ```
  
  isalpha()          # 判斷是否是英文字
  islower()          # 判斷是否是小寫字母
  isnumeric()        # 判斷是否是數字
  isdigit()          # 判斷是否是數字
  isupper()          # 判斷是否是數字
  
  find()             # 找到某個子字傳的index，失敗會回傳nane
  index()            # 找到某個子字傳的index，失敗會error
  
  lower()            # 轉為小寫
  upper()            # 轉小寫
  title()            # 每個字第一個字元轉大寫
  
  replace()          # 替換
  split()            # 切分
  strip()            # 移除頭尾空格
  ```



## 特殊演算法

### palindrome 

* 找到一個字串中最長的 palindrome 

  ```
  def longestPalindrome(self, input_string: str) -> str:
      # 1. 用特數字元插在中間，不用判斷奇數或偶數長度的回文
      input_string = "%"+"%".join([i for i in input_string]) +"%"
      # 計算最長的回文
      longest_palindrome = ""
      max_len = 0  # 計算長度時 回文的半徑 = 回文長度(沒有插入特殊符號前的)
      for i,c in enumerate(input_string):
          # 以每一個字作為回文的中心判斷是否有回文
      	  win_size = 0
      	  while i-win_size >= 0 and i+win_size < len(input_string):
      		    if input_string[i-win_size] != input_string[i+win_size]:
      			      break
      		    win_size+=1
      	  win_size-=1 # !! 因為前面是 先加在判斷 這裡要對win_size-1
          
          # 判斷是否要更新
      	  if max_len < win_size:
        	    max_len = win_size
        	    longest_palindrome = input_string[i-win_size:i+win_size+1]
  
      return longest_palindrome.replace("%","")
  ```


### cumulative sum
| 問題                                                         | 描述                                                         | 解法                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Range Sum Query 1D — Immutable **                          | Given nums = [-2, 0, 3, -5, 2, -1]<br>sumRange(0, 2) -> 1<br/>sumRange(2, 5) -> -1 <br/>sumRange(0, 5) -> -3 | cumulative sum 1D                                            |
| **Range Sum Query 2D — Immutable **                          | Given matrix = [  [3, 0, 1, 4, 2],   [5, 6, 3, 2, 1],   [1, 2, 0, 1, 5],   [4, 1, 0, 1, 7],   [1, 0, 3, 0, 5] ]<br/>sumRegion(2, 1, 4, 3) -> 8 <br/>sumRegion(1, 1, 2, 2) -> 11 <br/>sumRegion(1, 2, 2, 4) -> 12 | cumulative sum 2D                                            |
| [**Range Sum Query 1D — Mutable **](https://www.cnblogs.com/grandyang/p/4985506.html) | 同 Range Sum Query 1D — Immutable，array可能改變             | 1. 把一個 Array 分成幾個段落，cache memory 存的就是每個段落的總和。<br>2. segment Tree<br>3. Binary Indexed Tree (Fenwick) |
| [**Range Sum Query 2D — Mutable **](https://www.cnblogs.com/grandyang/p/5300458.html) | 同 Range Sum Query 2D — Immutable，array可能改變             | 1. 對 Row 或者 Col 做累加，求區間總和的時候就算出每個其中的 Row /Col 的區間總和再全部加起來<br/>2. segment Tree<br/>3. Binary Indexed Tree |



# Hash

把數值先記起來，之後在search時可以減少時間複雜度

*  Hash Table - avg O(1), worse(n)
    * compute the key's hash code
    * map the hash code to an index
```
(key)         (hash code)   (hash table)
"hi"  -------- 123 ----->   [0] -> hi -> abc ...
                            [1]
"hello" ------ 456 ---->    [2] -> hello
```
* 將 hash 建成 balance BST - O(logn)
* Additional Reading: Hash Table Collision Resolution (pg 636), Rabin-Karp Substring Search (pg 636).

# LeetCode 題目

| 問題                               | 描述                                                         | 解法                                                         |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 11. Container With Most Water | 給予不同高度牆壁的array求任兩個牆可以收集到最多的水量<br>Input: [1,8,6,2,5,4,8,3,7]  Output: 49 | Greedy, Two Point                                          |
| 41. First Missing Positive | 找到array中缺失的最大正數，時間Ｏ（n) 空間 Ｏ(1) | 對比值跟其index,迴圈將錯誤位子的值放到正卻的位子 |
| 227. Basic Calculator II  | Input: s = "3+2*2"  Output: 7 | stack, 數字前是+,-將數字放入stack,否則pop前一個數字做完運算再放入stack|
| 238. Product of Array Except Self  | 給予一個nums array 返回給個數除了本身以外的積 <br>input: [1,2,3,4] output: [24,12,8,6] <br>不可以用除法 | 每一個輸入數的積會是其前面數列的積乘上後面數列的積，分別由組數的兩端便利找到 accumulate product sum |
| 287. Find the Duplicate Number | 在 array 中找到唯一重複的數字，array中只會有1-len(array)的數字 | binary search + 鴿籠 / bit manipulation|
| 348. Design Tic-Tac-Toe | 設計佔格子連線的遊戲，是否可以在Ｏ(1)的時間內判斷是否有ｇ輸贏 | 計算每行每列以及對角線上雙方的棋子數，數量等於邊長實代表該方勝利 |
| 772. Basic Calculator III  | "2*(5+5*2)/3+(6/2+8)" = 21 | stack, 將括號裡的內容當成一個整體用遞歸處理, => 或者把中敘式處理成前後敘式|
| 378. Kth Smallest Element in a Sorted Matrix | Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return *the* `kth` *smallest element in the matrix*.<br>Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 <br>Output: 13 | 1. 排序後找<br>2. max heap<br>3. 在陣列的對大值和最小直間做Bibary Search，每次判斷陣列中小於mid的元素數量（由左下或右上開始找小於等於k的值）時間O(nlogX) X -> 最大最小值的差 |
| **315. Count of Smaller Numbers After Self** | 計算給定array中每一個數字的又變有幾個小於自己的數<br>Input: nums = [5,2,6,1] Output: [2,1,1,0] | 1. 用binary search 把數值由右往左插入新的array中，在新array中的index就是答案<br>2. 建立一個bunary search tree，每個node多一個smaller參數紀錄小於自己的數有多少個，在插入節點時更新路徑上節點的smaller |
| 406. Queue Reconstruction by Height | 給予一個people list，每一個people[i] = [h, k]，h代表該people的身高，k代表在正確的隊列中前面有幾個人比他高，將被短亂的list重建<br>Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] <br>Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] | 對list排序，依h高到低排序，如果身高一樣的話在根據k小到大排序：[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]<br>根據k將值依序插入一個新的隊列中，或是將沒排好的people往前移動 |

| 問題                          | 描述                                                         | 解法                                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 1. Two Sum                    | Given nums = [2, 7, 11, 15], target = 9, return [0, 1].      | 暴力解需要O(n**2)，使用hashr紀錄差值出現的位子減少查詢的時間複雜度O(n) |
|167. Two Sum II - Input array is sorted|Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.<br>Input: numbers = [2,7,11,15], target = 9<br/>Output: [1,2]|因為已經排序過，用two point|
|15. 3Sum|Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. <br>Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]|Sort 後用 兩個迴圈找到 two sum的結果，在用dict確認差值是否存在|
| 454. 4Sum II                  | Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] <br>Output: 2 <br>Explanation: <br>1. nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0 <br>2.  nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0 | two sum的延伸，使用hash將時間複雜度由Ｏ(n**4)降到O(n\*\*2) |
| 138. Copy List with Random Pointer|拷貝一個帶有隨機指針的list|取物件的id()作為hash的key|

# Cracking Interview

| 問題                               | 描述                                                         | 解法                                                         |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|Is Unique|Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?|1. sort<br>2 hash / array 紀錄之前看到過的字元<br>3.**用int作為array紀錄**|
|Check Permutation|Given two strings,write a method to decide if one is a permutation of the other.|1. 排序要個字串並比較<br>2. 用hash/array分別紀錄兩個字串出現過的字元，在比較是否相同<br>3. 用一個array紀錄一個加一個減最後確認是否全為零|
|URLify|Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)<br>Input: "Mr John Smith", 13 Output: Mr%20John%20Smith|先把最後一字元由個開始拷貝到字串最後，遇到空格則轉成%20，最後再將字串往前移|
|**Palindrome Permutation**|Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.|1. 用hash/array記錄每個字元出現的次數，如果都是偶數或只有一個奇數，代表是Palindrome Permutation <br>2. 使用bit紀錄，某個字元是是奇數的時候為1，某個字元是是偶數的時候為0，最後確認為1的bit是否<=1|
|**One Away**|There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.|1. Basic : [Edit Distance using Dynamic programming](https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/)，O(n^2) time<br>2. 用兩的point分別開始確兩個string，只能有一次不一樣(比對自傳長度判斷是修改、刪除、新增)，O(n) time、O(1)space|
|**String Compression**|Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).|1. 先做替換的動作，把重複的字換成字元加出現數量，剩下的換成符號-，之後再做一次移動的的動作，把字元移到前面|
|Rotate Matrix<br>48. Rotate Image|Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?|1. 由對角線翻轉，再由x軸翻轉 <br> 2. 繼算index轉換的規律，(i, j) <- (n-1-j, i) <- (n-1-i, n-1-j) <- (j, n-1-i)|
|Zero Matrix|Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.|1. 找到0之後把該行與列設成特殊符號，遍歷完矩陣後再替換掉 <br>2. 生成紀錄行與列是否要被置換成0的矩陣，遍歷完後mtrix後根據記錄矩陣將行獲列置換成0|
|**String Rotation**|Assume you have a method isSubstringwhich checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").|如果s1是s2的rotation，可以把s1=xy、s2=yx。把s2 double一下，那s2=yxyx，如果s2是s1 rotation的話，則s1一定會是s2的substring|