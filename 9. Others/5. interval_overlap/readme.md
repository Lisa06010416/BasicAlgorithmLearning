# Interval_overlap
給多組時間區段判斷是否有重複

## 常用技巧
1. 組數是否有排序
2. 把開始與結束的時間拆開，並分別對應＋／－１
    ```
    record_list = []
        for s, e in intervals:
            record_list.append((s, 1))
            record_list.append((e, -1))
   record_list = sorted(record_list)
   ```
   
## 題目

| 題目                                     | 說明                                                         | 解法 |
| ---------------------------------------- | ------------------------------------------------------------ | ---- |
| LeeCode : 435. Non-overlapping Intervals | 給一個intervals list 最少要刪掉多少的組數才能不重複 intervals = [[1,2],[2,3],[3,4],[1,3]]  => 1 (del [1, 2]) |      |
| LeeCode : 253. Meeting Rooms II          | 給一組時段的區間，代表會議的時間區段，判斷需要多少個會議室 [[0, 30],[5, 10],[15, 20]] => 2 |      |
|                                          |                                                              |      |

