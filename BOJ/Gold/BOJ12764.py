# https://www.acmicpc.net/problem/12764

# https://www.acmicpc.net/problem/12764

import heapq
x = int(input())
com = sorted(list(map(int, input().split())) for _ in range(x))

seat = [i for i in range(1, x + 1)]
hour = []

count = [0 for _ in range(x + 1)]
max_count = 0
for c in com:
    while hour and c[0] >= hour[0][0]:
        end_time, s = heapq.heappop(hour)
        heapq.heappush(seat, s)
    s = heapq.heappop(seat)
    heapq.heappush(hour, [c[1], s])
    max_count = max(max_count, len(hour))
    count[s] += 1

print(max_count)
for i in range(1, max_count+1):
  print(count[i], end=' ')