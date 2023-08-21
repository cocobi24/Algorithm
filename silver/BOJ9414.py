# https://www.acmicpc.net/problem/9414

import sys
input = sys.stdin.readline
money = 5*(10**6)
T = int(input())

land_list = []
for test in sys.stdin:
    land = int(test.rstrip())
    if land == 0 :
        land_list.sort(reverse=True)
        l = len(land_list)

        for i in range(l):
            land_list[i] = 2 * (land_list[i]**(i+1))
        total = sum(land_list)
        land_list = []

        print(total if money >= total else "Too expensive")
        continue
    land_list.append(land)