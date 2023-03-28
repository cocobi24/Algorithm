# https://www.acmicpc.net/problem/4134

import math
T = int(input())

def isPrime(n) :
    if n == 0 or n == 1 :
        return False
    for i in range(2, int(math.sqrt(n)+1)) :
        if n % i == 0 :
            return False
    return True

for _ in range(T) :
    N = int(input())
    while True :
        if isPrime(N) :
            break
        N += 1
    print(N)