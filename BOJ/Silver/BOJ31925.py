# https://www.acmicpc.net/problem/31925

import sys
input = sys.stdin.readline

n = int(input())

lst = [input().rstrip().split() for _ in range(n)]
lst = list(filter(lambda x: x[1] == 'jaehak' and x[2] == 'notyet' and (int(x[3]) == -1 or int(x[3]) > 3), lst))
lst = sorted(lst, key=lambda x: int(x[4]))[:10]
lst = sorted(lst, key=lambda x: x[0])
l = len(lst)

print(l)
for i in range(l):
    print(lst[i][0])