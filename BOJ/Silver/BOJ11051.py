# https://www.acmicpc.net/problem/11051

import math
n, k = map(int, input().split())
answer = math.comb(n, k) % 10007
print(answer, end='')