# https://www.acmicpc.net/problem/4948

import sys
input = sys.stdin

n=123456*2
a = [False, False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for n in input :
    n = int(n)
    if n == 0 :
        break
    temp = list(filter(lambda x : x > n and x <= 2*n, primes))
    print(len(temp))
