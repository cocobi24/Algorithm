# https://www.acmicpc.net/problem/26215

import heapq
n = int(input())
snow = list(map(int, input().split()))

heap = []
[ heapq.heappush(heap, (-s, s)) for s in snow ]

minute = 0
while len(heap) > 1 :
  first = heapq.heappop(heap)[1] - 1
  second = heapq.heappop(heap)[1] - 1
  if first > 0: heapq.heappush(heap, (-(first), first))
  if second > 0: heapq.heappush(heap,(-(second), second))
  minute += 1
if len(heap) > 0: minute += heapq.heappop(heap)[1]
print(minute if minute <= 1440 else -1)