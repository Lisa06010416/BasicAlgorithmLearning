from typing import List


"""435. Non-overlapping Intervals"""
class Solution:
    """給一個intervals list 最少要刪掉多少的組數才能不重複
    intervals = [[1,2],[2,3],[3,4],[1,3]]  => 1 (del [1, 2])
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        del_num = 0
        pre_index = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[pre_index][1]:  # 當前一個的尾 大於 後一個的 頭 ， 重複
                del_num += 1
                pre_index = i if intervals[i][1] < intervals[pre_index][1] else pre_index  # 刪掉尾最長的
            else:
                pre_index = i
        return del_num


"""253. Meeting Rooms II """
class solution:
    """ 給一組時段的區間，代表會議的時間區段，判斷需要多少個會議室
    [[0, 30],[5, 10],[15, 20]] => 2
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> bool:
        # 每有一個meeting開始，room數量要＋1，結束要-1
        # 將 intervals 處理成 時間對應增減room的tuple (time, +1/-1)，紀錄在record_list
        record_list = []
        for s, e in intervals:
            record_list.append((s, 1))
            record_list.append((e, -1))

        # sort record list
        record_list = sorted(record_list)

        # cal max room num
        room_num = 0
        max_room_num = 0
        for t, n in record_list:
            room_num += n
            max_room_num = max(max_room_num, room_num)
        return max_room_num


s = solution()
ans = s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print(ans)
