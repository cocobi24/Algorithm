# https://www.acmicpc.net/problem/2581

import math
M, N= int(input()), int(input())
primes = []

def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n)+1)) :
        if n % i==0:
            return False
    return True

for i in range(M, N+1) :
    if isPrime(i) :
        primes.append(i)

if len(primes) >= 1 :
    print(sum(primes), min(primes), sep="\n")
else :
    print(-1)