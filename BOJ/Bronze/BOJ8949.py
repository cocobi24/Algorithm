# https://www.acmicpc.net/problem/8949

a, b = map(str, input().split())
a, b = list(a), list(b)
l = len(a) if len(a) <= len(b) else len(b)

temp = []
for _ in range(l, 0, -1) :
    A, B = int(a.pop()), int(b.pop())
    temp.append(str(A + B))
temp.reverse()

answer = ''.join(a) + ''.join(b) + ''.join(temp)
print(answer)