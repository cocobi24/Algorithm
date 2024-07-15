# https://www.acmicpc.net/problem/1924

from collections import deque
x, y = map(int, input().split())
month = [[]]
days = deque(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

for i in range(12) :
    month.append([])
    day = 31
    if i == 1 :
        day = 28
    elif i == 3 or i == 5 or i == 8 or i == 10 :
        day = 30

    for j in range(day) :
        today = days.popleft()
        month[i].append(today)
        days.append(today)

print(month[x-1][y-1])