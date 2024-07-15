# https://www.acmicpc.net/problem/6219

A, B, D = map(int, input().split())

li = [1]*(B+1)
for i in range(2, int(B**0.5)+1):
    if li[i]:
        for j in range(i+i, B+1, i):
            li[j] = 0
primes = [i for i in range(A, B+1) if li[i]]

count = 0
for prime in primes:
    if str(D) in str(prime):
        count += 1
print(count)