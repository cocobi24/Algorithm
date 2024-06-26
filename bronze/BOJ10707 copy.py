# https://www.acmicpc.net/problem/10707

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

X = a * p
over = (p - c) * d if p > c else 0
Y = b + over
print(X if X < Y else Y)