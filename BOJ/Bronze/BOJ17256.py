# https://www.acmicpc.net/problem/17256

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
bx, by, bz = cx - az, cy // ay, cz - ax
print(bx, by, bz)