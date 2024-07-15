# https://www.acmicpc.net/problem/2530

h, m, s = map(int, input().split())
timer = int(input())
clock = [0, timer // 60, timer % 60]
clock[0] = clock[1] // 60
clock[1] = clock[1] % 60

h = (h + clock[0]) + (m + clock[1]) // 60
m = (m + clock[1]) % 60 + (s + clock[2]) // 60
s = (s + clock[2]) % 60

hh = h + m // 60
mm = m % 60 + s // 60
ss = s % 60

print(hh % 24, mm % 60, ss % 60)