# https://www.acmicpc.net/problem/11401

n, k = map(int, input().split())
p = 1000000007

def pow(a, b):
    if b == 0 :
        return 1
    if b % 2 :
        return (pow(a, b//2)**2 * a) % p
    else:
        return (pow(a, b//2)**2) % p

fact = [1 for _ in range(n+1)]

for i in range(2, n+1) :
    fact[i] = fact[i-1] * i % p

A = fact[n]
B = (fact[n-k] * fact[k]) % p

print((A % p) * (pow(B, p - 2) % p) % p)