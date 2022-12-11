# https://www.acmicpc.net/problem/11134

import math
t = int(input())

for _ in range(t) :
    n, c = map(int, input().split())
    print(math.ceil(n/c))
