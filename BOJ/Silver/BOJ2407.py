# https://www.acmicpc.net/problem/2407

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n-1)

n, m = map(int, input().split())
answer = factorial(n) // (factorial(m) * factorial(n-m))
print(answer, end='')
