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


##     