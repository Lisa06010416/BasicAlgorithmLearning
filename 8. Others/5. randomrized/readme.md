# Randomrized

## 題型

* Reservoir sampling
    
    * random sample k item from an linklist n(can't check len)
    ```
    from wiki
    從S中抽取首k項放入「水塘」中
    對於每一個S[j]項（j ≥ k）：
       隨機產生一個範圍從0到j的整數r
       若 r < k 則把水塘中的第r項換成S[j]項
  ```
  
* Shuffle
    * [洗牌的正确姿势-Knuth shuffle算法](https://yjk94.wordpress.com/2017/03/17/洗牌的正确姿势-knuth-shuffle算法/)



## Python 常用指令

### random

* random.seed (*a=None*, *version=2*)

* Interger

  * random.randint(*a*, *b*)
    * get a random int r, a <= r **<=b**

* Float

  * random.random()
    * random a float from 0.0 to 1.0
  * random.uniform(*a*, b)
    * random a float num r, a <= r **<= b**

* Sequence:

  * random.choice(*seq*)

    * 抽一個值

  * random.choices(*population*, *weights=None*, *, *cum_weights=None*, *k=1*)

    * 重複抽樣

  * random.sample(*population*, *k*, *, *counts=None*)

    * 不重複抽樣

  * random.shuffle(x)

    * Shuffle the sequence *x* **in place**

    