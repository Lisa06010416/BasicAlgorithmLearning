import heapq

s = [(5,6), (1,2), (3,4)]
heapq.heapify(s)
print(s)

a = heapq.heappop(s)
print(a)

heapq.heappush(s, (-1, 5))
print(s)