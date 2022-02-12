# Math

## 題型
* Implement math function
    * 50. Pow(x, n)
    * 69. Sqrt(x)
    * 372. Super Pow

## Permutation and Combination
* Permutation
    * P(n, m) = n! / (n-m)!
* Combination
    * C(n. m) = n! / (n-m)!*m!
* Cycle Permutation
    * cycle_p(n, m) = P(n, m)/m
* Combination with Repetition/Multicombination
    * 由n個不同類型中取m個物品，每種類型的數量大於m
    * H(n,m) = C(n+m-1, m)
    * (排列組合中的重複組合)[https://ddxu2.pixnet.net/blog/post/205885106]


## Probability
* conditional probability:
    * Independent :
        * P(A) = P(A^B)/P(B)  <=>  P(A^B) = P(B)*P(A)
    * No Independent :
        * P(A|B) = P(A^B)/P(B)  <=>   P(A^B) = P(A|B)*P(B)

* Bayes' theorem
    * P(Ai|B) = P(Ai^B) / P(B) = P(Ai)*P(Ai|B) / (P(A1)*P(A1|B + ... + P(Ak)*P(Ak|B)
    
## Pigeonhole principle
* k 個東西分成 n 類， 若 k > (n-1)r + 1 則有一類東西之數目大於或等於 r。
* question list:
    * -[] 287. Find the Duplicate Number

## Count Prime
get prime less than n
* 拉托斯特尼筛法 Sieve of Eratosthenes

## 透過log加速
* 題目：
    * Power of Three 
    
* log 常用公式



# python 浮點數計算問題


# python math
### math
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