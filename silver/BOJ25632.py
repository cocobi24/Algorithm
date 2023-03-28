# https://www.acmicpc.net/problem/25632

A, B = map(int, input().split())
C, D = map(int, input().split())

def creadte_primes(n, m) :
    li = [1] * (m+1)
    for i in range(2, int(m**0.5)+1) :
        if li[i] :
            for j in range(i+i, m+1, i) :
                li[j] = 0
    primes = [i for i in range(n, m+1) if li[i]]
    return set(primes)

yt_primes = creadte_primes(A, B)
yj_primes = creadte_primes(C, D)
common_primes = set(yt_primes) & set(yj_primes)

cnt = len(common_primes)
if cnt % 2 == 0 :
    print("yj" if len(yj_primes) >= len(yt_primes) else "yt")
else :
    print("yt" if len(yt_primes) >= len(yj_primes) else "yj")