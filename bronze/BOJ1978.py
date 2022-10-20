# https://www.acmicpc.net/problem/1978

import math

n = int(input())
temp = list(map(int, input().split()))
answer = 0

def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

for n in temp :
    flag = isPrime(n)
    if flag == True :
        answer += 1

print(answer, end='')