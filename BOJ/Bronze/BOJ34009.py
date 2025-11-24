# https://www.acmicpc.net/problem/34009

N = int(input())
A = sorted(map(int, input().split()), reverse=True)

print("Alice" if len(A) % 2 == 0 else "Bob")