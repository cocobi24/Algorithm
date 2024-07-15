# https://www.acmicpc.net/problem/2979

A, B, C = map(int, input().split())
parking = [0] * 100
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        parking[i] += 1
a = parking.count(1) * A
b = parking.count(2) * B * 2
c = parking.count(3) * C * 3
print(a + b + c)