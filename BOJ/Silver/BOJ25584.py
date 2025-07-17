# https://www.acmicpc.net/problem/25584

import sys
input = sys.stdin.readline

N = int(input())
count_set = {}
time = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        work = input().replace('-', '').rstrip().split()
        for w in work:
            if w in count_set:
                count_set[w] += time[i]
            else:
                count_set[w] = time[i]
time = count_set.values()
if len(time) == 0:
    print("Yes")
    exit()
print( "Yes" if max(time) - min(time) <= 12 else "No")