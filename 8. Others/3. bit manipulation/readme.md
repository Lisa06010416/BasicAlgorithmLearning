

# bit manipulation

Tips:
* 找不同：
    * 兩個完全相同的list只有一個不同 -> xor 可以找到
    * 如果不能確定其中一個list是什麼，則兩個
* 計算 ：
    * a >> 1 等於除二
    * a << 1 等於乘二
    * a ^ b 快速交換 a,b
    


## Bitwise Operator
|Operator |Name|Trick 1|Trick 2|Trick 3|
|:----|--------|-----|-----|-----|
|&|and|x & 0s = 0|x & 1s = x|x & x = x|
| \| |or      |x \| 0s = x|x \| 1s = 1s|x \| x =x|
|^|xor|x ^ 0s = x|x ^ 1s = ~x|x ^ x = 0|
| ~        | Not         |             |              |           |
| <<       | left shift  ||||
| >>       | right shift |             |              |           |



## Negative Numbers

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
  * (2)  2**n – x – 1

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

    

## Right Shift

* 第一種：logic right shift

  * 直接補0

  ```
     -3               6
  1 1 0 1  >> 1 => 0 1 1 0
  ```

* 第二種 ： Arithmetic right shift

  * 右移但是保留sign bit的值

  ```
     -3               -2
  1 1 0 1  >> 1 => 1 1 1 0
  ```



## Common Bit Task : Getting and Setting

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
  mask = (-1 << (1 + i))
	return num & mask
```

### Update Bit

```
def update_ith_bit(num, i, value):
    mask = ~(1 << i)
    return (num & mask) | (value << i)
```



