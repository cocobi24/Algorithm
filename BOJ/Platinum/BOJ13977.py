# https://www.acmicpc.net/problem/13977

import sys
input = sys.stdin.readline
M = int(input())
p = 1000000007
fact = [1] * 4000001
for idx in range(2, 4000001):
    fact[idx] = (fact[idx-1] * idx) % p

def pow(n, k):
    if k == 1:
        return n
    temp = pow(n, k//2)
    if k % 2 == 0:
        return (temp ** 2) % p
    else:
        return (temp ** 2 * n) % p

def inverse(n):
    return pow(fact[n], p-2)

for _ in range(M) :
    n, k = map(int, input().split())
    print((fact[n] * inverse(n-k) * inverse(k)) % p)