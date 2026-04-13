# https://www.acmicpc.net/problem/31712

yc, yd = map(int, input().split())
dc, dd = map(int, input().split())
pc, pd = map(int, input().split())
hp = int(input())

time = 0
while True:
    if time % yc == 0:
        hp -= yd
    if time % dc == 0:
        hp -= dd
    if time % pc == 0:
        hp -= pd

    if hp <= 0:
        break

    time += 1

print(time)