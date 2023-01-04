[cracking the interview <=> leetcode](https://ryanym.com/posts/ctci-on-leetcode/#chapter-8--recursion-and-dynamic-programming)

# Programming Learning

1. 描述問題，確認問題正確，問問題
    1. 分析多種方法講時間/空間複查度
2. 15分鐘一題medium，寫題時要描述作法

question:
* 回傳組合時是否可以排序
* 回傳多個index 是否可以重複
* 輸入值的特殊情況

##
數量 ：
* occurrence -> 出現次數
* xx's count
*  sorted into decreasing order of frequency of occurrence

## 解題紀錄
[解題紀錄](https://docs.google.com/spreadsheets/d/1Vgn7PrWuRJLGRGjoG0iS5nRqHqBfkUS8Y54vimAVZYc/edit#gid=0)

## 學習清單

### 演算法

* [演算法與資料結構](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)

### LeetCode 攻略

* [演算法電子書](https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/)
* [Leetcode常見題型即題目列表](https://zhuanlan.zhihu.com/p/341176507)

### Question List
* [Blind 75 Must Do Leetcode](https://leetcode.com/list/xi4ci4ig/)
* [Top Interview Questions](https://leetcode.com/explore/interview/card/top-interview-questions-medium/)
* [List of 2020 interview question for Google](https://leetcode.com/discuss/interview-question/971009/List-of-2020-interview-question-for-Google)

--------

## Python Tools

### Build-in Finction

#### Doc

[Built-in Functions](https://docs.python.org/3/library/functions.html)



#### number

* abs(n) - 絕對值

* round(n) - 四捨五入

  

#### positional numeral system - radix(base) change

* Binary/Octal/Hecadeciaml and Decimal

  ```
  # decimal to Binary
  bin(13)  -> "0b1101"
  # decimal t0 Octal
  oct(13) -> "0o15"
  # decimal t0 Hexadecimal
  hex(13) -> "0xd"
  
  # Binary/Octal/HexaDecimal to Decimal
  int("0b1101", 2)
  int("0o15", 8)
  int("0xd", 16)
  ```



#### Function mapping

* map(function, iterable, ...)

  ```
  map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) -> [3, 7, 11, 15, 19]
  ```

* filter(function, iterable)

  ```
  def is_odd(n):
      return n % 2 == 1
  
  newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> [1, 3, 5, 7, 9]
  ```

* reduce(function, iterable[, initializer])

  ```
  from functools import reduce
  def add(x, y) :           
      return x + y
  sum1 = reduce(add, [1,2,3,4,5])  -> 1+2+3+4+5 = 15
  ```

  

#### Object Info

```
# 記憶體位置
id(object)
# 列出 object 的 attribute
dir(object)
# 判斷object是否有attribute
hasattr(object, name)
# 取得屬性質
getattr(object, name)
# 取得說明
help(object)
```



-------

### re

[Doc](https://www.runoob.com/python/python-reg-expressions.html)



---

### math

[Python數學math模組55個函式詳解](https://www.gushiciku.cn/pl/pUPI/zh-tw)

* math.floor(n)/math.ceil(n) - 取上下界
* math.fsum(seq) - 比 sum 精準
* math.gcd(a,b) - 返回 a,b 的最大公約數 (greatest common divisor)
* math.log( x, base) - 取log
* math.sqrt(n) - 平方根 (square root)
* math.factoria(n) - 取 n 階乘



---

### Data Structure

#### deapq

```
data = [3,4,5]
heapq.heapify(data)
min = heapq.heappop(data)
heapq.heappush(data, 7)
```



