# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline
n = int(input())
workers = {}

for i in range(n) :
    worker = input().rstrip().split()[0]
    if worker not in workers :
        workers[worker] = 1
    else :
        workers.pop(worker)
workers = sorted(list(workers), reverse=True)
print('\n'.join(workers), end='')