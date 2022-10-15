# https://www.acmicpc.net/problem/15829

n = int(input())
str = list(input())
answer = 0

for i in range(n) :
    answer += (ord(str[i])-96) * 31**i
print(answer % 1234567891)