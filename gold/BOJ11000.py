# https://www.acmicpc.net/problem/11000

import sys, heapq
input = sys.stdin.readline
N = int(input())
timetable = sorted([list(map(int, input().split())) for _ in range(N)])

req_room = []
heapq.heappush(req_room, timetable[0][1])

for i in range(1, N) :
    if timetable[i][0] < req_room[0] :
        heapq.heappush(req_room, timetable[i][1])
    else :
        heapq.heappop(req_room)
        heapq.heappush(req_room, timetable[i][1])

answer = len(req_room)
print(answer)