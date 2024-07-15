# https://www.acmicpc.net/problem/1316

n = int(input())
answer = n

for i in range(n) :
    s = input()
    lenth = len(s)
    for j in range(lenth-1) :
        if s[j] == s[j+1] :
            pass
        elif s[j] in s[j+1:] :
            answer -= 1
            break

print(answer)