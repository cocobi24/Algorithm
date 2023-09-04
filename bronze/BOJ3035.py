# https://www.acmicpc.net/problem/3035

R, C, ZR, ZC = map(int, input().split())

for _ in range(R):
    row = list(input())
    s = ""
    for i in range(C):
        s += row[i]*ZC
    for _ in range(ZR):
        print(s)