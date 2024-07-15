# https://www.acmicpc.net/problem/1193

n = int(input())
rows = 1

while n > rows:
    n -= rows
    rows += 1

if rows % 2 == 0:
    col = n
    row = rows - n + 1
else:
    col = rows - n + 1
    row = n

print(col, '/', row, sep='')