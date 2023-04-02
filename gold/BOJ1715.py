# https://www.acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline
N = int(input())
card_list = []

if N == 0 :
    print(0)
else :
    for _ in range(N) :
        heapq.heappush(card_list, int(input()))

    compare = 0
    for i in range(N-1) :
        prev = heapq.heappop(card_list)
        current = heapq.heappop(card_list)
        temp = prev + current
        compare += temp
        heapq.heappush(card_list, temp)
    print(compare)