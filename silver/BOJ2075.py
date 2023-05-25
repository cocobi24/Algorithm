# https://www.acmicpc.net/problem/2075

import sys, heapq

input = sys.stdin.readline
N = int(input())
heap = []

nums = map(int, input().split())
for num in nums :
    heapq.heappush(heap, num)

for _ in range(1, N) :
    nums = map(int, input().split())
    for num in nums:
        heapq.heappush(heap, num)
        heapq.heappop(heap)

answer = heapq.heappop(heap)
print(answer)