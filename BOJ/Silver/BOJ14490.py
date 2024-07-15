# https://www.acmicpc.net/problem/14490

import math
n, m = map(int, input().split(':'))
gcd = math.gcd(n, m)
n = n//gcd
m = m//gcd
print(f"{n}:{m}", end='')