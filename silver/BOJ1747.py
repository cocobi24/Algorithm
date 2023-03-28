# https://www.acmicpc.net/problem/1747

import math
N = int(input())

def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n)+1)) :
        if n % i == 0 :
            return False
    return True

while True :
    if str(N) == str(N)[::-1] :
        if isPrime(N) :
            break
    N += 1

print(N)