# https://www.acmicpc.net/problem/2960

N, K = map(int, input().split())
nums = [i for i in range(2, N+1)]
primes = []

n = 2
while len(nums) != 0 :
    num = n
    if num in nums:
        nums.remove(num)
        primes.append(num)

    for i in range(n, N+1) :
        num = i*n
        if num in nums :
            nums.remove(num)
            primes.append(num)
        num = i
    n+=1

print(primes[K-1])