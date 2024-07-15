# https://www.acmicpc.net/problem/9020

T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)

li = [1] * 10001
for i in range(2, int(10000**0.5)+1) :
    if li[i] :
        for j in range(i+i, 10001, i) :
            li[j] = 0

for num in nums :
    n = num // 2
    m = n

    for _ in range(10000) :
        if li[n] and li[m] :
            print(n, m)
            break
        n -= 1
        m += 1