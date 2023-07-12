# https://www.acmicpc.net/problem/1735

def gcd(x, y):
    if y == 0:
        return x
    x, y = y, x % y
    return gcd(x, y)

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
N = gcd(A1*B2 + A2*B1, B1*B2)
print((A1*B2 + A2*B1)//N, B1*B2//N)