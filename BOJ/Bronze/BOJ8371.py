# https://www.acmicpc.net/problem/8371

n = int(input())
text1 = input().rstrip()
text2 = input().rstrip()

ans = 0
for i in range(n):
    if text1[i] != text2[i]:
        ans += 1

print(ans)