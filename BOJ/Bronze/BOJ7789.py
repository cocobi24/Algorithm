# https://www.acmicpc.net/problem/7789

import math
A, B = map(int, input().split())

def isPrime(n) :
    if n == 0 or n == 1 :
        return False
    for i in range(2, int(math.sqrt(n)+1)) :
        if n % i == 0 :
            return False
    return True

origin = isPrime(A)
new = isPrime(int(str(B)+str(A)))

if origin == True and new == True :
    print("Yes")
else :
    print("No")