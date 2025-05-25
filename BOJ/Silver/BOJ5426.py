# https://www.acmicpc.net/problem/5426

n = int(input())
for _ in range(n):
    string = list(input().rstrip())
    sqrt = int(len(string) ** (1/2))
    matric = []

    for idx in range(0, len(string), sqrt):
        matric.append(string[idx:idx+sqrt])

    ans = ''
    for i in range(sqrt):
        for j in range(sqrt):
            ans += matric[j][sqrt - 1 - i]
    print(ans)