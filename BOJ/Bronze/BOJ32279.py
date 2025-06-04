# https://www.acmicpc.net/problem/32279

n = int(input())
p, q, r, s = map(int, input().split())
a1 = int(input())

a = [0] * n
a[0] = a1
for i in range(1, n):
    if (i + 1) % 2 == 0:
        a[i] = p * a[(i - 1) // 2] + q
    else:
        a[i] = r * a[(i - 1) // 2] + s

print(sum(a))