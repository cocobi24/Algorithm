# https://www.acmicpc.net/problem/28444

H, I, A, R, C = map(int, input().split())
x = H * I
y = A * R * C
print(x-y)