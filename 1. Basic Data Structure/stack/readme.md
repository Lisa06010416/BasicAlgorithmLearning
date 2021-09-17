# Stack
一種後進先出(Last-In-First-Out)的結構

* 需要提供以下功能：
    * create
    * push
    * pop
    * isempty
    * isfull
    
* 解題時感到，前面的資訊會需要等後面的資訊才可以判斷，且會先需要比較近期才看過的資訊, ex
    * 括號匹配
    * expression evaluate

* 應用：
    * minstack
    * monotonic stack
    * DFS

* implement by array/linkinglist
    * 
    
## Monotone Stack
有兩種變化:
1. 比top小的值加入stack，比top大的值開始做處理 
2. 比top大的值加入stack，比top小的值開始做處理

**QP - stack 內的元素都是遞增或遞減**
    * [LeetCode Monotone stack](https://www.cnblogs.com/grandyang/p/8887985.html)  
    * [Monotone Questoin](Largest Rectangle in Histogram)
    
## stack permutation
給一組資料，藉由stack的push and pop出來，交換原本資料的前後順序

可能地爬序數量:
* Catalan number - 1/(n+1)*C(2n,n)
    * [證明](https://johnmayhk.wordpress.com/2014/02/03/cn/)
    * 一組資料 stack permutation 個數
    * n組括號的合法運算式的個數
    * n個節點組成不同構二元樹的方案數
    * 求一個2n位、含n個1、n個0的二進位數，滿足從左往右掃描到任意一位時，經過的0數不多於1數
    * n × n格點中不越過對角線的單調路徑的個數
    *通過連結頂點而將n + 2邊的凸多邊形分成三角形的方法個數。


## Infix, Prefix, Postfix
* Infix to Postfix
```
operator : */-
operand : 0,1,2...

While(Infix 還未結束):
    x = next_token(Infix)
    if x == operand: # 數字直接print
        print(x)
    else: # monotonic stack
        比較優先權 (X, stack.top) :
            ">" : stack.push(x) and break
            "<=" : repeat
                     y = pop(s)
                     print(y)
                   until x > stack.top
                   stack.push(x)
```

* evaluate postfix expresion
    * 可以忽略括號，由**左而右**掃描，當事數字時入stack，符號時pop，處理完再將新的數字入stack
           
* evaluate prefix expresion
    * preorder  - 可以忽略括號，由**右而左**掃描，當事數字時入stack，符號時pop，處理完再將新的數字入stack

* operator priority:
    括號 > 負號 > 幕次 > 乘除 > 加減 > 關係比較 > 邏輯 (not) > and/or >  assign