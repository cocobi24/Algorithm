# https://www.acmicpc.net/problem/31833

N = int(input())
A = int(''.join(list(input().rstrip().split())))
B = int(''.join(list(input().rstrip().split())))
print(min(A, B))