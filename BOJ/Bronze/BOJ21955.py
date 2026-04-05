# https://www.acmicpc.net/problem/21955

N = input().rstrip()
L = len(N) // 2
print(N[:L], N[L:])