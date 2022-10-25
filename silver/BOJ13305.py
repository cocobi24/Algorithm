# https://www.acmicpc.net/problem/13305

from collections import deque
n = int(input())
routes = deque(list(map(int, input().split())))
charge = deque(list(map(int, input().split())))
answer = 0

prev = charge.popleft()
while True :
    answer += routes.popleft() * prev
    if len(routes) == 0 :
        break

    temp = charge.popleft()
    if prev > temp :
        prev = temp

print(answer, end='')
