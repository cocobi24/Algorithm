# https://www.acmicpc.net/problem/15965

N = int(input())
INF = 10**7
temp = [1]*INF

for i in range(2, int(INF**0.5)+1) :
    if temp[i] :
        for j in range(i+i, INF, i) :
            temp[j] = 0

primes = [i for i in range(2, INF) if temp[i]]
print(primes[N-1])