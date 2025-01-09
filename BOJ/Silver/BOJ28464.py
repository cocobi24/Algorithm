# https://www.acmicpc.net/problem/28464

N = int(input())
poteto = sorted(map(int, input().split()))
idx = (N // 2) if N % 2 == 0 else (N // 2)
print(sum(poteto[:idx]), sum(poteto[idx:]))