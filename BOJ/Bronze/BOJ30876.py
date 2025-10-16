# https://www.acmicpc.net/problem/30876

import sys
input = sys.stdin.readline

N = int(input())
point_list = [list(map(int, input().split())) for _ in range(N)]
point_list.sort(key=lambda x: (x[1]))
print(*point_list[0])