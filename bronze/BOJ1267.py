# https://www.acmicpc.net/problem/1267

n = int(input())

seconds = list(map(int, input().split()))
y, m= 0, 0

for i in seconds :
    y += i//30 * 10 + 10
    m += i//60 * 15 + 15

answer = ("M" if y > m else "Y") if y != m else "Y M"
print(answer, min([y, m]))