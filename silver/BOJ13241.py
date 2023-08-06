# https://www.acmicpc.net/problem/13241

A, B = map(int, input().split())

def gcd(A, B):
    if B == 0:
        return A
    else:
        A %= B
        return gcd(B, A)

answer = (A * B) // gcd(A, B)
print(answer)