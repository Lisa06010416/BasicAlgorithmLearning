

# Bit Manipulation

## 7.1 Bitwise Operator

#### Bit Operator

|Operator |Name|Trick 1|Trick 2|Trick 3|Trick 4|
|:----|--------|-----|-----|-----|-----|
|&|and|x & 0s = 0|x & 1s = x|x & x = x||
| \| |or      |x \| 0s = x|x \| 1s = 1s|x \| x =x||
|^|xor|x ^ 0s = x|x ^ 1s = ~x|x ^ x = 0|交換 x,y : X^=Y, Y^=X, X^=Y|
| ~        | Not         |             |              |           ||
| <<       | left shift  |x*2 = x << 2|               |              ||
| \>>       | right shift | x/2 = x >> 2 |              |           ||

#### Useful Mask

| Mask         | Way                        |
| ------------ | -------------------------- |
| 1111...1111? | -1                         |
| 1111...1110? | -1 < 1                     |
| 00111?       | (1 < 3) - 1                |
| 111011?      | -1 ^ (1 << 2)<br>~(1 << 2) |
| 000100       | 1 << 2                     |
| 11100        | -1 << 2                    |
| 00011        | (1 << 3) - 1               |

#### Negative number

| Mask                                                         | Way                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| x = 110110 ，- x = ?                                         | ~x + 1 = 001001 + 1 = 001010                                 |
| x = -5 ，- x = ?                                             | ~(x - 1)                                                     |
| Get the rightest 1 of x ?  ex, x = 100110                    | x & (-x)<br>100110 & (011001 + 1) = 100110 & 011010 = 000010 |
| x > 0，x=3(0b011)<br>1's Complement of x?<br>2's Complement of x? | ~x = -0b100，x=-4<br>~x + 1=100 + 1 = 101,  x = -3           |
| x < 0，x=-3(-0b11)<br>-x = ?                                 | ~(x - 1)                                                     |
| 如何把一個負數的bit轉成對應的負數：<br>Res = 0b11111111111111111111111111111100 (32 bit) <br/>1's Complement of x? <br/>2's Complement of x? | MASK = 0xffffffff<br>MAX = 0x7fffffff<br>MIN = 0x80000000<br>if res > MAX:<br>    res = res ^ 0xffffffff = 00..011(3)<br/>    res = ~res = 111...100<br> |
| ~3, ~5 = ?<br>-3, -5 = ?                                     | python 的～去取not但同時會改變sign bit，導致實際的直會變成-x-1：-4(111...1100), -6(1111010)<br>-則是取two's complement: -3(111..1101), -5(111..1100) |
| 如何判斷一個數的sign bit是0還是1?                            | sb = x >> x.bit_length()<br>如果x>=0,sb=0, x<0,sb=1<img src="readme.assets/截圖 2023-05-01 下午4.52.53.png" alt="截圖 2023-05-01 下午4.52.53" style="zoom:50%;" /> |



## 7.2 Negative Numbers

### Ones’ Complement

| Decemal       | one's complement |
| ------------- | ---------------- |
| 2**(n-1) - 1  | 0111             |
| +1            | 0001             |
| +0            | 0000             |
| -0            | 1111             |
| -1            | 1110             |
| -2**(n-1) - 1 | 1000             |

* 轉換方式：

  * (1) Inverse number : 3 表示為: 0011， -3 表示為: 1100
  * (2)  2**n – x – 1 : 

* 減法 一樣可透過 加 一個『負數』來完成，但需要端回進位 (end around carry)：

  ```
  3 - 2 :
     0 0 1 1   (3)
  +  1 0 1 1   (-2)
  -----------
  1 | 0 0 0 0
            1
  -----------
      0 0 0 1
  ```

### Two’s Complement

| Decemal      | two's complement |
| ------------ | ---------------- |
| 2**(n-1) - 1 | 0111             |
| +1           | 0001             |
| 0            | 0000             |
| -1           | 1111             |
| -2**(n-1)    | 1000             |

* 1 的補數 仍具有兩個 0 (+0、-0)，加法器在做減法時，常需要一個額外的步驟，做端回進位。2 的補數 (Two’s Complement) 即可避免以上問題，整數表示、加法器的實作… 幾乎皆採用 2 的補數 表示法

*  轉換方式 ：

  * 1 的補數 + 1

  *  2***n – x (n 為位元數，x 為欲轉換正數)*

    

## 7.3 Right Shift

* 第一種：logic right shift

  * 直接補0

  ```
     -3               6
  1 1 0 1  >> 1 => 0 1 1 0
  ```

* 第二種 ： Arithmetic right shift

  * 右移但是保留sign bit的值
  * python

  ```
     -3               -2
  1 1 0 1  >> 1 => 1 1 1 0
  ```



## 7.4 Common Bit Task

* Getting, Setting, Clear(i, i_left, i_right), Update

### Get Bit

```
def get_ith_bit(num, i):
	return ((num & 1 << i) != 0)
```

### Set Bit

```
def set_ith_bit(num, i):
	return num | (1 << i)
```

### Clear Bit

```
def clear_ith_bit(num, i):
  mask = ~(1 << i)
	return num & mask

def clear_bit_left_than_ith(num, i):
  mask = (1 << i) - 1
	return num & mask
	
def clear_bit_right_than_ith(num, i):
  mask = ~(1 << (1 + i)) # or mask = -1 << (i + 1)
	return num & mask
```

### Update Bit

```
def update_ith_bit(num, i, value):
    mask = ~(1 << i)
    return (num & mask) | (value << i)
```



##  7.5 Problem



| Question                      | Description                                                  | Solution                                                     |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Inserting                     | Given two 32-bit numbers, N and M, and two-bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. Assuming index start from 0. <br>a)  N = 1024 (10000000000),     M = 19 (10011),     i = 2, j = 6      Output : 1100 (10001001100) |                                                              |
| **Binary fraction to String** | Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print” ERROR:’ | <img src="readme.assets/截圖 2023-01-20 下午5.34.46.png" alt="截圖 2023-01-20 下午5.34.46" style="zoom:150%;" /> |
| Flip Bit to Win               | You have an integer and you can flip exactly one bit from a 0 to a 1, Write code to find the length of the longest sequence of Is you could create. |                                                              |
| **Next Number**               | Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation. | <img src="readme.assets/截圖 2023-01-20 下午6.15.33.png" alt="截圖 2023-01-20 下午6.15.33" style="zoom:150%;" /> |
| Debugger                      | Explain what the following code does: ( (n & ( n - 1 ) ) == 0) | n = 4    100 & 011 == 0 <br>n=3      11 & 10 == 0<br>the code is used to check if n is 2, 4, 8, 16 ... (power of two) |
| Conversion                    | Write a function to determine the number of bits you would need to flip to convert integer A to integer B. |                                                              |
| PairwiseSwap                  | Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., 23 (**0**0**0**1**0**1**1**1), it should be converted to 43 (0**0**1**0**1**0**1**1**)). |                                                              |
| Draw Line                     | A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width `w`, where `w` is divisible by `8` (that is, no byte will be split across rows). The height of the screen, of course, can be derived from the length of the array and the width. Implement a function that draws a horizontal line from `(x1, y)` to (x2,  y) |                                                              |



### LeetCode Problem

#### Operator

| Question                     | Description                                                  | Solution                                                     |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **371. Sum of Two Integers** | 在不使用 + - 的情況下做兩數相加                              | 用bit做相加 ex 4(100) + 7(111) = 11(1011)  <br/>1.  不考慮進位 1 (1) ，做xor運算 <br/>2. 進位 10 (1010)，做 and運算在左移一位  <br/>3. 和剛好是1.2.兩數相加，要相加的部分在繼續重複1.2.直到2值為0  <br/>4. 負數的部分，調用 ＆ mask, 且最終的回傳值要用MAX判斷<img src="readme.assets/截圖 2023-05-01 下午3.23.30.png" alt="截圖 2023-05-01 下午3.23.30" style="zoom:150%;" /> |
| **16.9 Operations**:         | Write methods to implement the multiply, subtract, and divide operations for integers. The results of all of these are integers. Use only the add operator. | 1. Subtract: a + (-b)<br/><img src="../CrackingTheInterview_Exercise.assets/截圖 2023-04-05 下午3.26.43.png" alt="截圖 2023-04-05 下午3.26.43" style="zoom:50%;" /><br/>2. Multiply: add a b times, remember neg sign<br/>3. Divid: a - b until the ramainder is less than b |



#### Missing and Duplicate

| Question                           | Description                                                  | Solution                                                     |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **268. Missing Number**            | Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*<br>Input: nums = [3,0,1]<br/> Output: 2 | solution 1: 將少了一個數的nums跟完整的組數 xor，則相同的變為0，剩下的就是缺少的數<br>solution 2: 對組數再新增一個不服好，並把對應的數字放到相同的index中，最後符號所在的index就會是答案 |
| **287. Find the Duplicate Number** | Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.限制 : 不可以改變輸入的組數<br/>限制 : 也只能用 constant extra space<br/>Input: nums = [1,3,4,2,2] Output: 2 | solution 1: 鴿籠原理 + binary search <br/>solution 2: Bit Manipulation : 輸入數列在該bit上的1多於有序數列，代表重複的數字該bit會是1 |
| 136. Single Number                 | There is only **one repeated number** in `nums`, return *this repeated number*.Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.<br>You must implement a solution with a linear runtime complexity and use only constant extra space.<br>Input: nums = [2,2,1] Output: 1 | 1. 相同的數字xor: 4 ^ 4 = 0，因此把list中的每個數字xor，最後剩下的結果就是答案<img src="readme.assets/截圖 2023-04-24 下午9.59.34.png" alt="截圖 2023-04-24 下午9.59.34" style="zoom:50%;" /><br>2. 使用int紀錄每個數字出現的次數，由1變0者是答案 |
| 137. Single Number II              | Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*. <br>You must implement a solution with a linear runtime complexity and use only constant extra space. | 1. 用3個整數分別紀錄出先1,2,3次的數字<br>2. bit count and recover：紀錄每個bit出現的次數，並mod3<br><img src="readme.assets/截圖 2023-04-24 下午10.32.24.png" alt="截圖 2023-04-24 下午10.32.24" style="zoom:50%;" /> |
|                                    |                                                              |                                                              |
|                                    |                                                              |                                                              |



#### Other

| Question      | Description                                                  | Solution |
| ------------- | ------------------------------------------------------------ | -------- |
| 89. Gray Code | Given an integer `n`, return *any valid **n-bit gray code sequence***.<img src="readme.assets/截圖 2023-04-24 下午9.48.16.png" alt="截圖 2023-04-24 下午9.48.16" style="zoom:50%;" /> |          |