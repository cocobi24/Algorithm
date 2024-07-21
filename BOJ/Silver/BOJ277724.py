# https://www.acmicpc.net/problem/277724

import math

N, M, K = map(int, input().split())

match = int(math.log(N, 2))
ans = int(math.log(K, 2))
ans = min(ans + M, match)
print(ans)