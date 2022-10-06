# https://www.acmicpc.net/problem/5585

money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
answer = 0

for i in coins :
    answer += money // i
    money = money % i

print(answer)