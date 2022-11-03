# https://www.acmicpc.net/problem/1010

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n-1)

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m-n))
    print(answer)
