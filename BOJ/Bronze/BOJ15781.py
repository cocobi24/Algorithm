# https://www.acmicpc.net/problem/15781

N, M = map(int, input().split())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
print(max(H) + max(A))