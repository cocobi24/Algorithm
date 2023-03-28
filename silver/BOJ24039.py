# https://www.acmicpc.net/problem/24039

N = int(input())

limit = 104
temp = [1] * limit
for i in range(2, int(limit**0.5)+1) :
    if temp[i] :
        for j in range(i+i, limit, i) :
            temp[j] = 0
primes = [i for i in range(2, limit) if temp[i]]

for i in range(1, len(primes)) :
    num = primes[i-1]*primes[i]
    if num > N :
        print(num)
        break