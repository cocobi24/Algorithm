# https://www.acmicpc.net/problem/9613

import sys
import math
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    l = len(num_list)
    answer = 0
    for i in range(1, l):
        for j in range(i+1, l):
            answer += math.gcd(num_list[i], num_list[j])

    print(answer)