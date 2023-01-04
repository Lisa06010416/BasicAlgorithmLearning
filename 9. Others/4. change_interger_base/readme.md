## num base

* 負數轉成正數在做運算
* Python can solve arithmetic overflow, we don't need to care the range of integer
* 如果需要時做確認是否有超出界線 :
```
import sys
max_int, min_int = 2**31, -2**31 - 1
sign = 1 # 0 pos 1 neg
and_num = 0
if (base > int_max / 10) || 
   (base == int_max / 10 && and_num > 7)):
    if sign==1:
        base = int_min
    else:
        base = int_max

```
