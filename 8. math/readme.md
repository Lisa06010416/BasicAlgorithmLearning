

[TOC]



# 一、Math

## 1. Prime Numbers

* 每一個正整數都可以由prime number相乘組合出來
    ```
  87 = 2^2 * 3^1 * 5^0 * 7*1 ....
  ```
* 每一個正整數可以由4個以下的正整數的平方和組起來 

  ```
  13 = 9 + 4
  ```

* Dvisibility![截圖 2022-08-08 下午10.23.47](/Users/lisa/Learn/AlgorithmLearning/7. math/readme.assets/prime.png)



## 2. Probability

* conditional probability:
    * Independent :
        * P(A) = P(A^B)/P(B)  <=>  P(A^B) = P(B)*P(A)
    * No Independent :
        * P(A|B) = P(A^B)/P(B)  <=>   P(A^B) = P(A|B)*P(B)      
    
* Joint Probability
    * P(AvB) = P(A) + p(B) - P(A^B)
    
* Mutual Exclusivity 
    * P(AvB) = P(A) + p(B)
    * P(A^B) = 0
    
* Bayes' theorem
    
    ![截圖 2022-08-30 下午8.59.20](/Users/lisa/Learn/AlgorithmLearning/7. math/readme.assets/截圖 2022-08-30 下午8.59.20.png)



## 3. Permutation and Combination

* Permutation

  * P(n, m) = n! / (n-m)!

* Combination

  * C(n. m) = n! / (n-m)!*m!

* Cycle Permutation

  * cycle_p(n, m) = P(n, m)/m

* Combination with Repetition/Multicombination

  * 由n個不同類型中取m個物品，每種類型的數量大於m : H(n,m) = C(n+m-1, m)

    * 相當於在m個物品間放n-1個隔板區分類型，且隔板跟物品的不排列

  * 題目：

    * [十個圈圈跟兩個加號的排列數？](https://ddxu2.pixnet.net/blog/post/205885106)
    * [十個圈圈跟兩個加號排列時，加號左或右都要有圈圈](https://ddxu2.pixnet.net/blog/post/205885106)

    

  

## 二項式定理 與 多項式定理



## 常用數學公式    



## Pigeonhole principle

* k 個東西分成 n 類， 若 k > (n-1)r + 1 則有一類東西之數目大於或等於 r。
* question list:
  * 287. Find the Duplicate Number



## 透過log加速

* 題目：
  * Power of Three 

* log 常用公式

# 二、題目

## Prime Number

| 題目                       | 解法                                                         |
| -------------------------- | ------------------------------------------------------------ |
| 判斷 n 是否是 primality    | 確認 1 - sqrt(n) 中的值是否可以整除n，可以的話代表n不是prime |
| 找出數字Ｎ以下的prime list | 列出所有正整數。從2開始，刪掉2的倍數。找下一個未被刪掉的數字，找到3，刪掉3的倍數。找下一個未被刪掉的數字，找到5，刪掉5的倍數。如此不斷下去，就能刪掉所有合數，找到所有質數。 |



## 實作數學公式

| 題目           | 說明 | 解法 |
| -------------- | ---- | ---- |
| 50. Pow(x, n)  |      |      |
| 69. Sqrt(x)    |      |      |
| 372. Super Pow |      |      |



## Crack the interview 練習題

| 題目                       | 說明 | 解法                                                         |
| -------------------------- | ---- | ------------------------------------------------------------ |
|**The Heavy Pill**|You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once|https://wdxtub.com/interview/14520603230526.html|
|Basketball|You have a basketball hoop and someone says that you can play one of two games.<br/>Game 1: You get one shot to make the hoop.<br/>Game 2: You get three shots and you have to make two of three shots.<br/>If p is the probability of making a particular shot, for which values of p should you pick one game or the other?|https://www.geeksforgeeks.org/puzzle-basketball-shots/|
|Dominos|There is an 8x8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominos, and a single domino can cover exactly two squares. Can you use the 31 dominos to cover the entire board? Prove your answer (by providing an example or showing why it's impossible)|https://www.geeksforgeeks.org/puzzle-25chessboard-and-dominos/|
|Ants on a Triangle|There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed.<br/>Similarly, find the probability of collision with n ants on an n-vertex polygon|2^n - 2 / 2^n|
|Jugs of Water|You have a five-quart jug, a three-quart jug, and an unlimited supply of water (but no measuring cups). How would you come up with exactly four quarts of water? Note that the jugs areoddlyshaped,suchthatfillingupexactly"half"ofthejugwouldbeimpossible.|https://chanjarster.github.io/post/cracking-coding-interview/6.5-jugs-of-water/|
|Blue-Eyed Island|A bunch of people are living on an island, when a visitor comes with a strange order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at 8:00 pm every evening. Each person can see everyone else's eye color, but they do not know their own (nor is anyone allowed to tell them). Additionally, they do not know how many people have blue eyes, although they do know that at least one person does. How many days will it take the blue-eyed people to leave?|if has m blue eyes -> m days|
|The Apocalypse|In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy-that is, they have continue to have children until they have one girl, at which point they immediately stop-what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.|One way to think about this is to imagine that we put all the gender sequences of each family into one giant string. So if family 1 has BG, family 2 has BBG, and family 3 has G, it would be BGBBGG. Therefore, the gender ratio is 50% girls and 50% boys.|
|**The Egg Drop Problem**|There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break. If it's dropped from any floor below, it will not break. You're given two eggs. Find N, while minimizing the number of drops for the worst case.|[14](https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/)|
|**100 Lockers**|There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?|[10 lockers are left open](https://www.braingle.com/brainteasers/teaser.php?op=2&id=7824&comm=0)|
|**Poison**|You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible?|2^10 = 1024, so bottle 1 is 0000000001 -> one drop to strip 1; bottle 2 is 0000000010 -> one drop to strip 2. Using the strips as the binary bit, after 1000 drops we can know which bottle contains poison.|





# 三、Ｍath in Python

## python 負數計算問題

* python 負數的//與％是向負無限取整數，教學(https://blog.csdn.net/sun___M/article/details/83142126)
   ```
   -5 // 2 = -3
   5 // -2 = -3
  -5 % 2 =
  ```



## python 浮點數計算問題

### build-in

```
round(1,111, 2) = 1.11

# 會有不精準的問題
# 這是因為在電腦內部，1.115 真正的值是 1.11499999999999999111
round(1.115, 2) = 1.11
```

### Decimal

    * 提供十進位的運算，精確度(precision)、約整(rounding)等等
    * 最好用字串建立Decimal物件
    ```
    from decimal import Decimal
    a = 1.115
    Decimal(a)
    # Decimal(a) 的值和想像中的不同
    Decimal('1.1149999999999999911182158029987476766109466552734375')
    b = 1.125
    Decimal(b)
    # Decimal(b) 的值則和想像中一樣
    Decimal('1.125')
    ```
    * quantize :
      * 將一個浮點數，依指示的有效位數進行約整(rounding，或稱捨入)
        ```
        Decimal('1.115').quantize(Decimal('.00'), ROUND_HALF_UP)
        ## 得到 Decimal('1.12')，結果與我們想像中的相同
        1.12，可以直接用 print 輸出
        
        ## 錯誤的使用方式，使用「浮點數」型態建立 Decimal
        Decimal(1.115).quantize(Decimal('.00'), ROUND_HALF_UP)
        ## 錯誤，原因與之前使用 round 函數時相同
        Decimal('1.11')
        ````



## python math library

    * math.floor(n)/math.ceil(n) - 取上下界
    * math.fsum(seq) - 比 sum 精準
    * math.gcd(a,b) - 返回 a,b 的最大公約數 (greatest common divisor)
    * math.log( x, base) - 取log
        ```
        math.log(27, 3) = 3.0
        # 會有不精準的問題
        math.log(243, 3) = 4.999999
        ```
    * math.sqrt(n) - 平方根 (square root)
    * math.factoria(n) - 取 n 階乘

